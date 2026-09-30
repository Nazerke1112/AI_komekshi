import streamlit as st
import sqlite3, json, ast, subprocess, sys, tempfile, os
from datetime import date, timedelta
import pandas as pd
import altair as alt

st.set_page_config(page_title='AI көмекшісі — Python үйрену платформасы', page_icon='🐍', layout='wide', initial_sidebar_state='expanded')
DB='pystart.db'
AUTHOR='Бердібек Назерке'

# ========================= DATA =========================
LESSONS=[
('🐍','Python-ға кіріспе','Python негіздері',
'Python — оқуға жеңіл синтаксисі бар жоғары деңгейлі бағдарламалау тілі. Ол білім беру, веб-жасау, автоматтандыру, деректер және AI салаларында қолданылады.',
'Python есепті алгоритмге айналдырып, компьютерге нақты нұсқаулар беруге көмектеседі. Бастапқы кезеңде print(), айнымалылар, шарттар, циклдер және функциялар негізгі құралдар болады.',
'print("Сәлем, Python!")\nprint(2 + 3)',
['1-жол print() арқылы мәтінді шығарады.','2-жол Python 2 + 3 өрнегін есептейді.','Мәтін тырнақша ішінде жазылады.'],
'print сөзін Print деп жазу — Python регистрге сезімтал.',
'print() — компьютердің экран арқылы жауап беруі сияқты.',
'Python кодын кішкентай қадамдарға бөліп жаз.',
'5 * 2',['7','10','25','3'],'10','5 × 2 = 10.',
[('Easy','Hello Python! мәтінін шығар.','print("Hello Python!")','Hello Python!'),('Medium','12 + 8 нәтижесін шығар.','print(12 + 8)','20'),('Challenge','Python үйреніп жатқаның туралы сөйлем шығар.','print("Мен Python үйреніп жатырмын!")','Мен Python үйреніп жатырмын!')],
'print("Python басталды")','print("Python басталды")','Бастапқы код дұрыс. Синтаксисті сақта.',
[('Python-да экранға мәтін шығаратын функция?', ['input()','print()','type()','range()'],'print()'),('Python регистрге сезімтал ма?',['Иә','Жоқ','Тек сандарда','Тек мәтінде'],'Иә'),('2 + 3?', ['5','6','23','1'],'5'),('Мәтінді әдетте неге аламыз?',['Жақшаға','Тырнақшаға','Қос нүктеге','Үтірге'],'Тырнақшаға'),('print() не істейді?',['Мәтін енгізеді','Экранға нәтиже шығарады','Цикл жасайды','Файл өшіреді'],'Экранға нәтиже шығарады')]),
('📦','Айнымалылар және мәліметтер типтері','Variables & Types',
'Айнымалы — белгілі мәнді сақтайтын атаулы орын. Python мән берілген кезде оның типін анықтайды. Негізгі типтер: int, float, str, bool.',
'Айнымалылар деректерді сақтауға және қайта пайдалануға мүмкіндік береді. Сан мен мәтінді шатастырма: 16 — int, "16" — str.',
'name="Dana"\nage=16\nscore=92.5\npassed=True\nprint(name)\nprint(age)',
['name — str мәтіні.','age — int бүтін саны.','score — float ондық саны.','passed — bool логикалық мәні.'],
'"16" — мәтін, ал 16 — сан.',
'Айнымалыны аты жазылған қорап ретінде елестет.',
'str пен int-ті тікелей қоспа; қажет болса int() немесе str() қолдан.',
'age = 16\nage = age + 1\nprint(age)',['16','17','15','161'],'17','16 + 1 = 17.',
[('Easy','name айнымалысына ат сақта.','name="Dana"\nprint(name)','Dana'),('Medium','price=1200, count=3. Жалпы құнын шығар.','price=1200\ncount=3\nprint(price*count)','3600'),('Challenge','Ат, жас және баллды бөлек шығар.','student="Dana"\nage=16\nscore=95\nprint(student)\nprint(age)\nprint(score)','Dana\n16\n95')],
'score="90"\nprint(score+10)','score=90\nprint(score+10)','score сан болуы керек.',
[('16 қандай тип?',['str','float','int','bool'],'int'),('"Hello" қандай тип?',['int','str','float','bool'],'str'),('True қандай тип?',['bool','int','str','list'],'bool'),('Ондық сан?',['7','7.5','"7.5"','True'],'7.5'),('Айнымалы жасау?',['x == 5','x = 5','5 = x','var x 5'],'x = 5')]),
('⌨️','Input және математикалық амалдар','Input & Math',
'input() пайдаланушыдан мән қабылдайды және бастапқыда str қайтарады. int(), float() арқылы санға түрлендіруге болады. +, -, *, /, //, %, ** негізгі арифметикалық операторлар.',
'Input бағдарламаны интерактивті етеді. Пайдаланушыдан сан алғанда int(input(...)) үлгісі жиі қолданылады.',
'a=int(input("a = "))\nb=int(input("b = "))\nprint(a+b)',
['input() енгізуді алады.','int() мәтінді бүтін санға түрлендіреді.','a+b қосу амалын орындайды.'],
'input() нәтижесі str болғандықтан, санмен амал алдында түрлендір.',
'input() — бағдарлама мен адам арасындағы сұрақ-жауап терезесі.',
'input() → str. Сан керек болса int(input(...)) қолдан.',
'a=10\nb=3\nprint(a//b)\nprint(a%b)',['3 және 1','3 және 0','3.33 және 1','4 және 2'],'3 және 1','// бүтін бөлуді, % қалдықты береді.',
[('Easy','15 пен 5 қосындысын шығар.','a=15\nb=5\nprint(a+b)','20'),('Medium','Ұзындығы 8, ені 5 тік төртбұрыш ауданын есепте.','length=8\nwidth=5\nprint(length*width)','40'),('Challenge','2500 теңгеге 10% жеңілдік жаса.','price=2500\ndiscount=price*0.10\nprint(price-discount)','2250.0')],
'age=input("Жас: ")\nprint(age+1)','age=int(input("Жас: "))\nprint(age+1)','input() нәтижесін int-ке түрлендір.',
[('input() қандай тип қайтарады?',['int','str','bool','float'],'str'),('7 // 2?',['3','3.5','1','4'],'3'),('7 % 2?',['3','1','0','2'],'1'),('Көбейту операторы?',['x','*','%','//'],'*'),('Санға түрлендіру?',['str()','bool()','int()','list()'],'int()')]),
('🔀','if / elif / else шарттары','Conditions',
'Шартты операторлар бағдарламаға жағдайға байланысты шешім қабылдауға мүмкіндік береді. if негізгі шартты, elif қосымша шартты, else қалған жағдайды өңдейді.',
'Шарттар балл деңгейін анықтау, санның таңбасын тексеру сияқты көптеген есептердің негізі.',
'score=75\nif score>=90:\n    print("A")\nelif score>=70:\n    print("B")\nelse:\n    print("C")',
['score 75 болады.','90>= шарт жалған.','70>= шарт ақиқат, сондықтан B шығады.'],
'= мән тағайындайды, == салыстырады. if жолынан кейін : қажет.',
'Шартты бағдарламадағы бағдаршам сияқты: жағдайға қарай бір бағыт таңдалады.',
'if/elif/else блоктарында : және дұрыс шегініс маңызды.',
'score=80\nif score>=90:\n    print("A")\nelif score>=70:\n    print("B")\nelse:\n    print("C")',['A','B','C','Ештеңе'],'B','80 саны 70-тен үлкен, бірақ 90-нан кіші.',
[('Easy','number оң болса Positive, әйтпесе Negative шығар.','number=5\nif number>0:\n    print("Positive")\nelse:\n    print("Negative")','Positive'),('Medium','90+ A, 70+ B, 50+ C, қалғаны F.','score=82\nif score>=90:\n    print("A")\nelif score>=70:\n    print("B")\nelif score>=50:\n    print("C")\nelse:\n    print("F")','B'),('Challenge','Санның оң, теріс немесе нөл екенін анықта.','number=-4\nif number>0:\n    print("Positive")\nelif number<0:\n    print("Negative")\nelse:\n    print("Zero")','Negative')],
'score=80\nif score>50\n    print("Pass")','score=80\nif score>50:\n    print("Pass")',': белгісін және шегіністі түзет.',
[('Салыстыру операторы?',['=','==',':=','==='],'=='),('if соңында?',[':',';','.',','],':'),('Қалған жағдай?',['if','elif','else','for'],'else'),('90>=80?',['True','False','90','80'],'True'),('AND операторы?',['and','or','not','plus'],'and')]),
('🔁','for / while циклдері','Loops',
'Цикл бір әрекетті бірнеше рет орындауға арналған. for тізбек элементтерін аралайды, while шарт True болғанша қайталанады.',
'Цикл қайталанатын жұмысты автоматтандырады. range(5) 0,1,2,3,4 мәндерін береді.',
'for i in range(1,6):\n    print(i)',
['range(1,6) 1-ден 5-ке дейін береді.','i әр қайталануда жаңа мән алады.','print(i) сол мәнді шығарады.'],
'range(5) 0-ден 4-ке дейін береді, соңғы шекара кірмейді.',
'Цикл — бір тапсырманы бірнеше рет орындайтын күн тәртібі сияқты.',
'for — тізбекпен жұмысқа, while — шартқа тәуелді қайталауға ыңғайлы.',
'for i in range(3):\n    print(i)',['1 2 3','0 1 2','0 1 2 3','3 3 3'],'0 1 2','range(3) 0,1,2 береді.',
[('Easy','1-ден 5-ке дейін шығар.','for i in range(1,6):\n    print(i)','1\n2\n3\n4\n5'),('Medium','1-ден 10-ға дейінгі жұп сандарды шығар.','for i in range(2,11,2):\n    print(i)','2\n4\n6\n8\n10'),('Challenge','1-ден 100-ге дейінгі сандар қосындысын тап.','total=0\nfor i in range(1,101):\n    total+=i\nprint(total)','5050')],
'for i in range(5)\n    print(i)','for i in range(5):\n    print(i)',': белгісін ұмытпа.',
[('range(3)?',['1,2,3','0,1,2','0,1,2,3','3'],'0,1,2'),('Цикл не үшін?',['Қате','Қайталанатын әрекет','Файл','Тек мәтін'],'Қайталанатын әрекет'),('while қашан?',['Шарт True','Бір рет','False','Ешқашан'],'Шарт True'),('range(2,8,2) соңғысы?',['6','8','7','2'],'6'),('for соңында?',[':',';','==','='],':')]),
('📋','List','Тізімдер',
'List — бірнеше мәнді бір реттелген құрылымда сақтайтын коллекция. Элементтер [] ішінде жазылады, индекс 0-ден басталады.',
'Көп дерекпен жұмыс істегенде list ыңғайлы. append() соңына элемент қосады, len() элементтер санын береді.',
'scores=[90,75,88,100]\nprint(scores[0])\nscores.append(95)\nprint(scores)',
['scores[0] — бірінші элемент.','append(95) соңына 95 қосады.','Индекс 0-ден басталады.'],
'Бірінші индекс 1 емес, 0.',
'List — бірнеше зат салынған реттелген қораптар қатары сияқты.',
'Индекс 0-ден басталады; append() соңына қосады.',
'numbers=[10,20,30]\nprint(numbers[1])',['10','20','30','1'],'20','Индекс 1 — екінші элемент.',
[('Easy','Үш жемісті list жасап, біріншісін шығар.','fruits=["apple","banana","orange"]\nprint(fruits[0])','apple'),('Medium','scores ішіндегі max мәнді шығар.','scores=[70,92,84,100]\nprint(max(scores))','100'),('Challenge','numbers ішіндегі жұп сандар санын циклмен тап.','numbers=[3,8,10,5,12,7]\ncount=0\nfor n in numbers:\n    if n%2==0:\n        count+=1\nprint(count)','3')],
'numbers=[10,20,30]\nprint(numbers[3])','numbers=[10,20,30]\nprint(numbers[2])','Үш элемент индексі 0,1,2.',
[('List жақшасы?',['()','[]','{}','<>'],'[]'),('Бірінші индекс?',['0','1','-1','2'],'0'),('Соңына қосу?',['add()','append()','push()','insert_end()'],'append()'),('Элементтер саны?',['count_all()','len()','size()','length()'],'len()'),('max([3,9,2])?',['2','3','9','14'],'9')]),
('⚙️','Functions','Функциялар',
'Функция — қайта пайдалануға болатын код бөлігі. Ол def арқылы анықталады. Параметрлер дерек қабылдайды, return нәтиже қайтарады.',
'Функциялар кодты бөліктерге бөледі, қайталануды азайтады және жобаны түсінікті етеді.',
'def add(a,b):\n    return a+b\n\nprint(add(5,3))',
['def add(a,b) функцияны анықтайды.','return нәтижені қайтарады.','add(5,3) функцияны шақырады.'],
'Функцияны анықтау оны автоматты түрде іске қоспайды — оны шақыру керек.',
'Функция — қайта-қайта қолданылатын дайын құрал.',
'def → анықтау, parameter → кіріс дерек, return → нәтиже.',
'def square(x):\n    return x*x\nprint(square(4))',['8','12','16','4'],'16','4 × 4 = 16.',
[('Easy','Екі санды қосатын add функциясын жаз.','def add(a,b):\n    return a+b\nprint(add(2,5))','7'),('Medium','Сан квадратын қайтаратын square жаз.','def square(x):\n    return x*x\nprint(square(6))','36'),('Challenge','Үш бағаның орташа мәнін қайтаратын average жаз.','def average(a,b,c):\n    return (a+b+c)/3\nprint(average(80,90,100))','90.0')],
'def add(a,b)\n    return a+b','def add(a,b):\n    return a+b',': белгісін қос.',
[('Функцияны анықтайтын сөз?',['func','def','function','make'],'def'),('Нәтижені қайтару?',['give','return','send','back'],'return'),('add(2,3) не?',['Функцияны шақыру','Айнымалы','Цикл','Шарт'],'Функцияны шақыру'),('Параметр қайда?',['def кейін жақшада','print ішінде','return кейін','if ішінде'],'def кейін жақшада'),('Функция пайдасы?',['Кодты қайталауды азайту','Қатені көбейту','Тек мәтін','Тек цикл'],'Кодты қайталауды азайту')]),
('🐞','Debugging','Қатемен жұмыс',
'Debugging — бағдарламаның қателерін табу, себебін түсіну және түзету процесі. Error message мәселенің түрі мен орнын анықтауға көмектеседі.',
'Қате — үйренудің бөлігі. Жүйелі әдіс: хабарламаны оқу → жолды табу → себепті анықтау → түзету → қайта тексеру.',
'score="80"\nprint(score+10)',
['score str ретінде сақталған.','str пен int тікелей қосылмайды.','score=int(score) деп түрлендіруге болады.'],
'Error хабарламасын оқымай кодты кездейсоқ өзгерту debugging-ті қиындатады.',
'Debugging — симптомнан себепті іздейтін диагностика сияқты.',
'Қате шықса, error type және line нөміріне назар аудар.',
'numbers=[1,2,3]\nprint(numbers[1])',['1','2','3','Қате'],'2','Индекс 1 — екінші элемент.',
[('Easy','if синтаксистік қатесін түзет.','x=7\nif x>5:\n    print(x)','7'),('Medium','str пен int қатесін түзет.','age="16"\nprint(int(age)+1)','17'),('Challenge','List соңғы элементін қауіпсіз шығар.','items=["A","B","C"]\nprint(items[-1])','C')],
'score=80\nif score>50\n    print("Pass")','score=80\nif score>50:\n    print("Pass")',': белгісі жоқ.',
[('Debugging дегеніміз?',['Дизайн','Қатені табу және түзету','Аударма','Файл'],'Қатені табу және түзету'),('TypeError?',['Тип мәселесі','Интернет','Экран','Файл'],'Тип мәселесі'),('IndexError?',['Индекс мәселесі','Атау','print','комментарий'],'Индекс мәселесі'),('Бірінші қадам?',['Error хабарламасын оқу','Өшіру','Кодты өшіру','Интернет'],'Error хабарламасын оқу'),('Қате жасау пайдалы ма?',['Иә','Жоқ','Тек күрделі кодта','Тек тестте'],'Иә')]),
('🧠','Algorithm және Problem Solving','Алгоритмдер',
'Алгоритм — есепті шешуге апаратын реттелген қадамдар жиыны. Problem solving есепті түсіну, бөлу, алгоритм құру, кодтау және тексеруді қамтиды.',
'Код жазудан бұрын Input → Process → Output моделін анықтау есепті кішкентай бөліктерге бөлуге көмектеседі.',
'scores=[70,80,90]\ntotal=0\nfor score in scores:\n    total+=score\naverage=total/len(scores)\nprint(average)',
['Input — scores.','Process — бағаларды қосу және бөлу.','Output — орташа балл.'],
'Есепті толық түсінбей кодты бірден бастау жиі қате.',
'Алгоритм — межеге жету картасы сияқты.',
'Күрделі есепті шағын қадамдарға бөл.',
'numbers=[2,4,6]\ntotal=0\nfor n in numbers:\n    total+=n\nprint(total)',['6','10','12','14'],'12','2+4+6=12.',
[('Easy','Екі сан қосындысының алгоритмін кодта.','a=4\nb=6\nresult=a+b\nprint(result)','10'),('Medium','max() қолданбай ең үлкен санды тап.','numbers=[4,12,7,19,3]\nbiggest=numbers[0]\nfor n in numbers:\n    if n>biggest:\n        biggest=n\nprint(biggest)','19'),('Challenge','List ішіндегі оң сандар қосындысын тап.','numbers=[-2,5,7,-1,4]\ntotal=0\nfor n in numbers:\n    if n>0:\n        total+=n\nprint(total)','16')],
'numbers=[4,8,2]\nbiggest=0\nfor n in numbers:\n    if n>biggest:\n        biggest=n\nprint(biggest)','numbers=[4,8,2]\nbiggest=numbers[0]\nfor n in numbers:\n    if n>biggest:\n        biggest=n\nprint(biggest)','Бастапқы мәнді list-тен алған дұрыс.',
[('Алгоритм?',['Реттелген қадамдар жиыны','Тек Python','Тек формула','Мәтін'],'Реттелген қадамдар жиыны'),('IPO?',['Input Process Output','Integer Python Object','Input Print Only','Idea Program Output'],'Input Process Output'),('Есепті бөлудің пайдасы?',['Күрделілікті азайту','Қатені көбейту','Кодты жою','Дизайн'],'Күрделілікті азайту'),('Ең үлкенді іздеу?',['Салыстыру','Тек print','Тек input','Тек str'],'Салыстыру'),('Problem solving қашан?',['Есепті түсінуден','Аяқтағаннан','Тесттен кейін','Дизайннан'],'Есепті түсінуден')]),
('🚀','Final Project — Student Grade Analyzer','Қорытынды жоба',
'Final Project — барлық негізгі Python ұғымдарын бір бағдарламада біріктіретін практикалық жоба. Student Grade Analyzer оқушы бағаларын талдайды.',
'Жоба input, variables, list, loops, if/elif/else, functions және arithmetic ұғымдарын біріктіреді.',
'def average(scores):\n    return sum(scores)/len(scores)\nscores=[80,90,75]\nprint(average(scores))',
['scores бағаларды list ретінде сақтайды.','average() орташа мәнді есептейді.','sum()/len() орташа мәнді береді.'],
'Барлық кодты бір үлкен блокқа жазбай, функцияларға бөл.',
'Final Project — бұрынғы құралдардың барлығын бір құрылғыға жинау сияқты.',
'Жобаға кіріспес бұрын input, process, output және функцияларды жоспарла.',
'scores=[80,90,100]\nprint(sum(scores)/len(scores))',['80','90','100','270'],'90.0','(80+90+100)/3 = 90.',
[('Easy','scores орташа мәнін есепте.','scores=[80,90,100]\nprint(sum(scores)/len(scores))','90.0'),('Medium','average нәтижесіне қарай Excellent/Good/Needs practice шығар.','average=82\nif average>=90:\n    print("Excellent")\nelif average>=70:\n    print("Good")\nelse:\n    print("Needs practice")','Good'),('Challenge','Student Grade Analyzer шағын нұсқасын жаса.','def analyze(name,scores):\n    avg=sum(scores)/len(scores)\n    print("Student:",name)\n    print("Average:",avg)\n    print("Max:",max(scores))\n    print("Min:",min(scores))\n    if avg>=90:\n        print("Level: Excellent")\n    elif avg>=70:\n        print("Level: Good")\n    else:\n        print("Level: Needs practice")\nanalyze("Dana",[90,85,95])','Student: Dana\nAverage: 90.0\nMax: 95\nMin: 85\nLevel: Excellent')],
'def average(scores)\n    return sum(scores)/len(scores)','def average(scores):\n    return sum(scores)/len(scores)',': белгісін қос.',
[('Final Project не біріктіреді?',['Негізгі Python ұғымдарын','Тек print','CSS','HTML'],'Негізгі Python ұғымдарын'),('Орташа формула?',['sum / len','max / min','len / sum','sum * len'],'sum / len'),('Ең жоғары баға?',['min()','max()','high()','top()'],'max()'),('Функцияның пайдасы?',['Кодты құрылымдау','Қатені жасыру','Дизайн','print'],'Кодты құрылымдау'),('Жобаның мақсаты?',['Үйренгенді практикада біріктіру','Тек тест','Видео','Мәтін'],'Үйренгенді практикада біріктіру')])
]

# ========================= VIDEO LIBRARY =========================
# Әр сабаққа YouTube видеосының URL-ын осы жерден ауыстыруға болады.
# Мысалы: https://www.youtube.com/watch?v=VIDEO_ID
VIDEO_LIBRARY=[
    ('Python-ға кіріспе — Python деген не?', 'https://youtu.be/la_FZsaFIT0?si=NbM9iVzcmPAV2Onw'),
    ('Айнымалылар және мәліметтер типтері', 'https://youtu.be/COttdgjedPs?si=Uv7a_NH0RP4SRY3g'),
    ('Input және математикалық амалдар', 'https://youtu.be/C2i_1fz-owU?si=chv3ZbWSmmyTrQz-'),
    ('if / elif / else шарттары', 'https://youtu.be/GCciXDE37Tc?si=M_PVMA8iOgS0J07r'),
    ('for / while циклдері', 'https://youtu.be/3pIHU8dQfmA?si=5faLpO8ceK7ASlSH'),
    ('List — тізімдермен жұысм', 'https://youtu.be/2SkxiG58JTk?si=v7t6S5Eo3qi1D11U'),
    ('Functions — функциялар', 'https://youtu.be/ohawYNNmKYM?si=Jr2HyNdzj1sqRSfn'),
]

# Convert tuples to dicts for readable access
D=[]
for i,x in enumerate(LESSONS,1):
    icon,title,short,definition,why,example,explain,mistake,analogy,remember,pcode,popts,pans,pexp,tasks_,broken,fixed,dexp,quiz_=x
    video_title,video_url=VIDEO_LIBRARY[i-1] if i-1<len(VIDEO_LIBRARY) else (title,'')
    D.append(dict(id=i,icon=icon,title=title,short=short,definition=definition,why=why,example=example,explain=explain,mistake=mistake,analogy=analogy,remember=remember,predict_code=pcode,predict_options=popts,predict_answer=pans,predict_explain=pexp,tasks=tasks_,broken=broken,fixed=fixed,debug_explain=dexp,quiz=quiz_,video_title=video_title,video_url=video_url))

# ========================= DB =========================
def conn():
    c=sqlite3.connect(DB,check_same_thread=False); c.row_factory=sqlite3.Row; return c

def init_db():
    c=conn()
    c.execute('''CREATE TABLE IF NOT EXISTS student_progress(
        name TEXT PRIMARY KEY, xp INTEGER DEFAULT 0, streak INTEGER DEFAULT 1, last_day TEXT,
        completed TEXT DEFAULT '[]', scores TEXT DEFAULT '{}', errors TEXT DEFAULT '[]',
        achievements TEXT DEFAULT '[]', solved INTEGER DEFAULT 0, correct INTEGER DEFAULT 0,
        attempts INTEGER DEFAULT 0, study_minutes INTEGER DEFAULT 0, video_watched TEXT DEFAULT '{}')''')
    c.commit(); c.close()

def norm_name(n):
    return ' '.join(n.split()).title()

def register(name):
    c=conn()
    c.execute('INSERT OR IGNORE INTO student_progress(name,last_day) VALUES(?,?)',(name,str(date.today())))
    c.commit(); c.close()

def load(name):
    c=conn(); r=c.execute('SELECT * FROM student_progress WHERE name=?',(name,)).fetchone(); c.close()
    return {'xp':r['xp'],'streak':r['streak'],'last_day':r['last_day'],'completed':json.loads(r['completed']),'scores':json.loads(r['scores']),'errors':json.loads(r['errors']),'achievements':json.loads(r['achievements']),'solved':r['solved'],'correct':r['correct'],'attempts':r['attempts'],'study_minutes':r['study_minutes'],'video_watched':json.loads(r['video_watched'] or '{}')}

def save():
    s=st.session_state; c=conn()
    c.execute('''UPDATE student_progress SET xp=?,streak=?,last_day=?,completed=?,scores=?,errors=?,achievements=?,
        solved=?,correct=?,attempts=?,study_minutes=?,video_watched=? WHERE name=?''',
        (s.xp,s.streak,s.last_day,json.dumps(s.completed,ensure_ascii=False),json.dumps(s.scores,ensure_ascii=False),
         json.dumps(s.errors,ensure_ascii=False),json.dumps(s.achievements,ensure_ascii=False),
         s.solved,s.correct,s.attempts,s.study_minutes,json.dumps(s.video_watched,ensure_ascii=False),s.student))
    c.commit(); c.close()

def init_state():
    register(st.session_state.student)
    d=load(st.session_state.student)
    for k,v in d.items(): st.session_state[k]=v
    defaults={'page':'Басты бет','lesson':1,'lesson_view':False,'hints':{},'task_done':{},'debug_done':{}}
    for k,v in defaults.items(): st.session_state.setdefault(k,v)

def xp(n): st.session_state.xp=max(0,st.session_state.xp+n); save()
def accuracy(): return round(st.session_state.correct/st.session_state.attempts*100) if st.session_state.attempts else 0
def pct(): return round(len(st.session_state.completed)/10*100)
def update_streak():
    t=date.today()
    try: last=date.fromisoformat(st.session_state.last_day)
    except Exception: last=t
    if last!=t:
        st.session_state.streak=st.session_state.streak+1 if last==t-timedelta(days=1) else 1; st.session_state.last_day=str(t); save()
def log_error(topic,msg):
    if not any(e['topic']==topic and e['message']==msg for e in st.session_state.errors): st.session_state.errors.append({'topic':topic,'message':msg,'date':str(date.today())}); save(); achievements()
def achievements():
    a=set(st.session_state.achievements)
    if st.session_state.solved>=1:a.add('First Code')
    if st.session_state.streak>=7:a.add('7 Day Streak')
    if len(st.session_state.errors)>=10:a.add('Bug Hunter')
    if st.session_state.solved>=20:a.add('Problem Solver')
    if 10 in st.session_state.completed:a.add('Final Project')
    st.session_state.achievements=sorted(a); save()

# ========================= SAFE RUNNER =========================
BLOCKED={'__import__','eval','exec','open','compile','globals','locals','vars','getattr','setattr','delattr','breakpoint','help','quit','exit'}
MODULES={'os','sys','subprocess','socket','requests','urllib','shutil','pathlib','ctypes','pickle','importlib'}
def run(code):
    if len(code)>6000:return False,'Код тым ұзын.'
    try: tree=ast.parse(code)
    except SyntaxError as e:return False,f'SyntaxError: {e}'
    for n in ast.walk(tree):
        if isinstance(n,ast.Name) and n.id in BLOCKED:return False,f'{n.id} қауіпсіздік мақсатында бұғатталған.'
        if isinstance(n,ast.Import) and any(a.name.split('.')[0] in MODULES for a in n.names):return False,'Бұл импорт қауіпсіз демонстрациялық режимде бұғатталған.'
        if isinstance(n,ast.ImportFrom) and (n.module or '').split('.')[0] in MODULES:return False,'Бұл импорт бұғатталған.'
    f=None
    try:
        with tempfile.NamedTemporaryFile('w',suffix='.py',delete=False,encoding='utf-8') as h:
            h.write(code); f=h.name
        r=subprocess.run([sys.executable,f],capture_output=True,text=True,timeout=3,cwd=os.getcwd())
        out=(r.stdout+r.stderr).strip() or 'Бағдарлама нәтиже шығармады.'
        return r.returncode==0,out
    except subprocess.TimeoutExpired:return False,'⏱️ Код 3 секундтан ұзақ орындалды.'
    except Exception as e:return False,str(e)
    finally:
        if f and os.path.exists(f):
            try:os.remove(f)
            except Exception:pass

def css():
    st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap');
:root{--bg:#07111f;--panel:rgba(15,29,49,.82);--border:rgba(126,167,215,.18);--muted:#91a4bc;--blue:#4da3ff;--yellow:#ffd54a;--green:#45d483;--red:#ff647c}
html,body,[class*="css"]{font-family:Inter,sans-serif}.stApp{background:radial-gradient(circle at 15% 10%,rgba(77,163,255,.13),transparent 30%),radial-gradient(circle at 85% 20%,rgba(255,213,74,.08),transparent 25%),linear-gradient(135deg,#06101d,#091526 55%,#07101c);color:#f4f8ff}.block-container{max-width:1400px;padding-top:2rem}[data-testid="stSidebar"]{background:linear-gradient(180deg,#081322,#07101c);border-right:1px solid var(--border)}
.brand-title{font-family:'Space Grotesk';font-size:27px;font-weight:800}.brand-title span{color:var(--yellow)}.brand-sub,.muted,.small{color:var(--muted);font-size:12px}.hero{border:1px solid var(--border);background:linear-gradient(135deg,rgba(22,43,72,.9),rgba(11,24,42,.8));border-radius:28px;padding:36px;box-shadow:0 24px 70px rgba(0,0,0,.25)}.hero h1{font-family:'Space Grotesk';font-size:clamp(34px,5vw,58px);line-height:1.03;letter-spacing:-2px;margin:12px 0}.hero p{color:#b7c7da;line-height:1.7}.eyebrow{color:var(--yellow);font-size:12px;font-weight:800;letter-spacing:2px}.glass{background:linear-gradient(145deg,rgba(19,37,61,.86),rgba(11,25,43,.72));border:1px solid var(--border);border-radius:20px;padding:22px;box-shadow:0 12px 40px rgba(0,0,0,.18)}.stat-label{color:var(--muted);font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:1px}.stat-value{font-family:'Space Grotesk';font-size:29px;font-weight:800}.section-title{font-family:'Space Grotesk';font-size:25px;font-weight:700;margin:28px 0 14px}.lesson-card{min-height:145px;transition:.2s}.lesson-card:hover{transform:translateY(-3px);border-color:rgba(77,163,255,.45)}.lesson-num{color:var(--blue);font-size:11px;font-weight:800}.lesson-name{font-family:'Space Grotesk';font-size:18px;font-weight:700;margin:7px 0}.badge{display:inline-block;border-radius:999px;padding:5px 10px;font-size:11px;font-weight:700;background:rgba(77,163,255,.1);color:#a8d1ff}.badge.done{color:#92f0ba;background:rgba(69,212,131,.09)}.badge.lock{color:#a4afbd;background:rgba(150,160,175,.08)}.road{border:1px solid var(--border);background:rgba(15,31,52,.86);border-radius:18px;padding:18px;display:flex;align-items:center;gap:15px}.road.current{border-color:rgba(77,163,255,.55)}.road-status{margin-left:auto;color:var(--muted);font-size:12px}.road-line{height:28px;width:3px;background:rgba(77,163,255,.25);margin:auto}.theory{color:#c7d4e4;line-height:1.8}.memory{border-left:4px solid var(--yellow);background:rgba(255,213,74,.07);border-radius:0 15px 15px 0;padding:17px}.video{min-height:170px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px dashed rgba(126,167,215,.3);border-radius:18px;color:var(--muted)}.video b{font-size:40px;color:var(--blue)}.ok{background:rgba(69,212,131,.08);border:1px solid rgba(69,212,131,.22);border-radius:15px;padding:15px}.bad{background:rgba(255,100,124,.08);border:1px solid rgba(255,100,124,.22);border-radius:15px;padding:15px}.info{background:rgba(77,163,255,.08);border:1px solid rgba(77,163,255,.2);border-radius:15px;padding:15px}div.stButton>button{width:100%;border-radius:13px!important;border:1px solid rgba(126,167,215,.22)!important;background:linear-gradient(135deg,rgba(27,51,80,.92),rgba(15,31,52,.92))!important;color:#edf5ff!important;font-weight:700!important;min-height:44px!important;transition:.18s!important}div.stButton>button:hover{transform:translateY(-1px);border-color:rgba(77,163,255,.6)!important;box-shadow:0 8px 25px rgba(0,0,0,.18)}div.stButton>button[kind="primary"]{background:linear-gradient(135deg,#2f8cff,#2565d8)!important;border:none!important}.stProgress>div>div>div>div{border-radius:999px}hr{border-color:rgba(126,167,215,.12)}
</style>''',unsafe_allow_html=True)

# ========================= RENDER =========================
def stat(icon,label,value):st.markdown(f'<div class="glass"><div style="font-size:22px">{icon}</div><div class="stat-label">{label}</div><div class="stat-value">{value}</div></div>',unsafe_allow_html=True)
def level():
    x=st.session_state.xp
    return '🚀 Python Creator' if x>=1600 else '🧠 Problem Solver' if x>=1000 else '💻 Python Developer' if x>=600 else '🔎 Python Explorer' if x>=250 else '🐣 Python Beginner'

def login_page():
    css()
    st.markdown(f'<div class="hero"><div class="eyebrow">PYTHON • LEARN • BUILD</div><h1>AI көмекшісі 🤖</h1><p>Платформаға кіру үшін аты-жөніңізді жазыңыз. Жаңа оқушы автоматты түрде тіркеледі, ал бұрын тіркелген оқушы прогресін жалғастырады.</p><p class="small">Жоба құрастырушысы: <b>{AUTHOR}</b></p></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔑 Кіру / Тіркелу</div>',unsafe_allow_html=True)
    name=st.text_input('Оқушының аты-жөні',placeholder='Мысалы: Айдос Серіков',key='login_name')
    if st.button('Кіру',type='primary',key='login'):
        n=norm_name(name)
        if len(n.split())<2:
            st.error('Аты мен тегін толық жазыңыз (кемінде екі сөз).')
        else:
            register(n); st.session_state.student=n; st.rerun()

def sidebar():
    with st.sidebar:
        st.markdown('<div class="brand-title">AI <span>көмекшісі</span> 🤖</div><div class="brand-sub">Python үйрену платформасы</div><br>',unsafe_allow_html=True)
        items=['🏠  Басты бет','🗺️  Roadmap','📚  Сабақтар','💻  Практика','🐞  Қатемен жұмыс','📊  Менің прогресім','🏆  Жетістіктер','🏅  Рейтинг','🚀  Final Project','🔬  Жоба туралы']
        labels=[x.split('  ',1)[1] for x in items]; cur=labels.index(st.session_state.page) if st.session_state.page in labels else 0
        pick=st.radio('Навигация',items,index=cur,label_visibility='collapsed'); st.session_state.page=pick.split('  ',1)[1]
        st.markdown('---'); st.markdown(f'**{level()}**'); st.progress(pct()/100); st.caption(f'⚡ {st.session_state.xp} XP  •  🔥 {st.session_state.streak} күн')
        st.markdown(f'👤 **{st.session_state.student}**')
        if st.button('🚪 Шығу',key='logout'):
            st.session_state.clear(); st.rerun()

def card(lesson):
    done=lesson['id'] in st.session_state.completed; unlocked=lesson['id']==1 or lesson['id']-1 in st.session_state.completed
    status='✓ Аяқталды' if done else ('→ Қолжетімді' if unlocked else '🔒 Құлыптаулы')
    cls='done' if done else ('lock' if not unlocked else '')
    st.markdown(f'<div class="glass lesson-card"><div class="lesson-num">{lesson["id"]:02d} / 10</div><div class="lesson-name">{lesson["icon"]} {lesson["title"]}</div><div class="muted">{lesson["short"]}</div><br><span class="badge {cls}">{status}</span></div>',unsafe_allow_html=True)

def dashboard():
    update_streak()
    st.markdown(f'<div class="hero"><div class="eyebrow">PYTHON • LEARN • BUILD</div><h1>Python-ды үйрен.<br>Код жаз. Жоба жаса.</h1><p>Сәлем, <b>{st.session_state.student}</b>! AI көмекшісі — теориядан практикаға, қателермен жұмысқа, тестке және нақты жобаға апаратын интерактивті оқу платформасы.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Сенің прогресің</div>',unsafe_allow_html=True); c=st.columns(4)
    for col,args in zip(c,[('⚡','XP',st.session_state.xp),('🔥','Streak',f'{st.session_state.streak} күн'),('📚','Сабақтар',f'{len(st.session_state.completed)}/10'),('🎯','Дұрыс жауап',f'{accuracy()}%')]):
        with col:stat(*args)
    nxt=next((x for x in D if x['id'] not in st.session_state.completed),D[-1]); st.markdown('<div class="section-title">Оқуды жалғастыру</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="glass"><h3>{nxt["icon"]} {nxt["title"]}</h3><p class="muted">{nxt["short"]}</p></div>',unsafe_allow_html=True)
    if st.button('▶  Оқуды жалғастыру',type='primary',key='continue'):
        st.session_state.lesson=nxt['id'];st.session_state.page='Сабақтар';st.session_state.lesson_view=True;st.rerun()
    st.markdown('<div class="section-title">🔥 Daily Challenge</div>',unsafe_allow_html=True); st.markdown('<div class="info">1-ден 100-ге дейінгі жұп сандарды шығар. <b>+50 XP</b></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Adaptive Learning</div>',unsafe_allow_html=True)
    weak=[(int(k),v) for k,v in st.session_state.scores.items() if v<80]
    if not weak:
        st.markdown('<div class="ok">✨ 80%-дан төмен нәтиже жоқ. Келесі тақырыпқа дайынсың!</div>',unsafe_allow_html=True)
    else:
        w=D[min(weak,key=lambda z:z[1])[0]-1]['title']
        st.markdown(f'<div class="info">💡 Әлсіз тақырып: {w}. Қайталау ұсынылады.</div>',unsafe_allow_html=True)

def roadmap():
    st.title('🗺️ Roadmap'); st.caption('Алдыңғы сабақты аяқтаған сайын келесі кезең ашылады.')
    for l in D:
        done=l['id'] in st.session_state.completed; unlocked=l['id']==1 or l['id']-1 in st.session_state.completed
        cur='current' if unlocked and not done else ''
        stt='✅ Аяқталды' if done else ('🔄 Қазір' if unlocked else '🔒 Құлыптаулы')
        st.markdown(f'<div class="road {cur}"><span style="font-size:27px">{l["icon"]}</span><div><b>{l["title"]}</b><div class="small">{l["short"]}</div></div><div class="road-status">{stt}</div></div>',unsafe_allow_html=True)
        if unlocked and not done and st.button(f'🚀 {l["title"]} бастау',key=f'road{l["id"]}'):
            st.session_state.lesson=l['id'];st.session_state.page='Сабақтар';st.session_state.lesson_view=True;st.rerun()
        if l['id']<10:st.markdown('<div class="road-line"></div>',unsafe_allow_html=True)

def video(l):
    st.markdown('<div class="section-title">🎬 Видеосабақ</div>',unsafe_allow_html=True)
    watched=st.session_state.video_watched.get(str(l['id']),False)
    st.markdown(f'<div class="glass"><div class="eyebrow">VIDEO LESSON {l["id"]:02d}</div><h3 style="margin:8px 0 4px">🎥 {l["video_title"]}</h3><div class="small">YouTube • шамамен 5–15 минут</div></div>',unsafe_allow_html=True)
    if l['video_url']:
        st.video(l['video_url'])
        if watched:
            st.markdown('<div class="ok">✅ <b>Видеосабақ көрілді</b><br><span class="small">Бұл видео прогресіңе белгіленді.</span></div>',unsafe_allow_html=True)
        elif st.button('✓ Видеоны көрдім  +10 XP',type='primary',key=f'video_seen_{l["id"]}'):
            st.session_state.video_watched[str(l['id'])]=True
            xp(10)
            save()
            st.rerun()
    else:
        st.markdown('<div class="video"><b>▶</b><strong>YouTube видеосы дайын емес</strong><span class="small">VIDEO_LIBRARY ішіндегі осы сабақтың video_url жолына YouTube URL енгізіңіз.</span></div>',unsafe_allow_html=True)
        st.info('💡 YouTube сілтемесін қосқаннан кейін preview автоматты түрде осы жерде ашылады.')

def playground():
    st.markdown('<div class="section-title">💻 Python Playground</div>',unsafe_allow_html=True); st.markdown('<div class="info">Қауіпсіз демонстрациялық режим: қауіпті модульдер бұғатталған, орындалу уақыты 3 секунд.</div>',unsafe_allow_html=True)
    code=st.text_area('Код',value='x=10\ny=20\nprint(x+y)',height=190,key='play')
    if st.button('▶ Кодты іске қосу',type='primary',key='run'):
        ok,out=run(code)
        if ok:
            st.session_state.solved+=1;xp(5);achievements();st.markdown(f'<div class="ok"><b>Output</b><pre>{out}</pre></div>',unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bad"><b>Қате</b><pre>{out}</pre></div>',unsafe_allow_html=True);log_error('Python Playground',out)

def tasks(l):
    st.markdown('<div class="section-title">🧩 Практикалық тапсырмалар</div>',unsafe_allow_html=True)
    icons={'Easy':'🟢','Medium':'🟡','Challenge':'🔴'}
    hints=['Алдымен негізгі операцияны анықта.','Қажетті айнымалы/цикл/шартты таңда.','Күтілетін нәтижемен салыстыр.']
    rewards={'Easy':10,'Medium':20,'Challenge':40}
    for i,(lev,prompt,solution,expected) in enumerate(l['tasks']):
        with st.expander(f'{icons[lev]} {lev} • {prompt}',expanded=i==0):
            st.markdown(f'**Шарт:** {prompt}<br>**Expected output:** `{expected}`',unsafe_allow_html=True)
            code=st.text_area('Код',value=solution if i==0 else '# Кодты осында жаз',height=170,key=f'task{l["id"]}_{i}')
            hk=f'{l["id"]}_{i}'; h=st.session_state.hints.get(hk,0)
            if h:st.markdown(f'<div class="info">💡 Hint {h}: {hints[h-1]}</div>',unsafe_allow_html=True)
            a,b=st.columns(2)
            with a:
                if st.button('💡 Hint',key=f'h{hk}'):
                    st.session_state.hints[hk]=min(3,h+1);xp(-3 if h<2 else 0);st.rerun()
            with b:
                if st.button('✓ Тексеру',key=f'check{hk}'):
                    ok,out=run(code);st.session_state.attempts+=1
                    if ok and out.strip()==expected.strip():
                        st.session_state.correct+=1;st.session_state.solved+=1;xp(rewards[lev]);st.session_state.task_done[hk]=True;achievements();st.success(f'Дұрыс! +{rewards[lev]} XP')
                    else:
                        st.session_state.task_done[hk]=False;log_error(l['short'],f'{lev}: {out}');st.error('❌ Әлі дұрыс емес.');st.code(out)

def debugging(l):
    st.markdown('<div class="section-title">🐞 Қатені тап</div>',unsafe_allow_html=True);st.code(l['broken'])
    code=st.text_area('Түзетілген код',value=l['broken'],height=150,key=f'debug{l["id"]}')
    if st.button('✓ Қатені тексеру',key=f'db{l["id"]}'):
        if ''.join(code.split())==''.join(l['fixed'].split()):
            xp(20);st.session_state.solved+=1;st.session_state.debug_done[l['id']]=True;achievements();st.success('✅ Қате түзетілді! +20 XP');st.info(l['debug_explain'])
        else:
            log_error(l['short'],l['debug_explain']);st.error('❌ Әлі дұрыс емес. Синтаксиске назар аудар.')

def quiz(l):
    st.markdown('<div class="section-title">📝 Mini Test</div>',unsafe_allow_html=True); answers=[]
    for i,(q,opts,ans) in enumerate(l['quiz']):answers.append(st.radio(q,opts,key=f'q{l["id"]}_{i}'))
    if st.button('📊 Тест нәтижесін шығару',type='primary',key=f'quiz{l["id"]}'):
        score=sum(a==x[2] for a,x in zip(answers,l['quiz'])); p=score*20
        st.session_state.scores[str(l['id'])]=p;st.session_state.attempts+=5;st.session_state.correct+=score
        xp(30 if score==5 else 15 if score>=3 else 0);save();st.success(f'{score}/5 — {p}%')

def lesson():
    l=D[st.session_state.lesson-1]; unlocked=l['id']==1 or l['id']-1 in st.session_state.completed
    if not unlocked:st.warning('🔒 Алдыңғы сабақты аяқтау керек.');return
    st.markdown(f'<div class="hero"><div class="eyebrow">LESSON {l["id"]:02d} / 10</div><h1>{l["icon"]} {l["title"]}</h1><p>{l["short"]} • Теория → Видео → Болжа → Код → Практика → Debugging → Test</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Теория</div>',unsafe_allow_html=True);a,b=st.columns([1.5,1])
    with a:
        st.markdown('**Анықтама**');st.markdown(f'<div class="theory">{l["definition"]}</div>',unsafe_allow_html=True);st.markdown('**Не үшін керек?**');st.markdown(f'<div class="theory">{l["why"]}</div>',unsafe_allow_html=True);st.markdown('**Синтаксис / мысал**');st.code(l['example'],language='python')
    with b:
        st.markdown('<div class="glass"><b>Мысалдың әр жолы</b></div>',unsafe_allow_html=True)
        for x in l['explain']:st.markdown('• '+x)
        st.markdown(f'<div class="bad"><b>🐞 Жиі қате</b><br>{l["mistake"]}</div>',unsafe_allow_html=True);st.markdown(f'<div class="info"><b>Өмірдегі аналогия</b><br>{l["analogy"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="memory"><b>💡 Есте сақта:</b> {l["remember"]}</div>',unsafe_allow_html=True);video(l)
    st.markdown('<div class="section-title">🧪 Кодты болжа</div>',unsafe_allow_html=True);st.code(l['predict_code']);ans=st.radio('Нәтиже қандай?',l['predict_options'],key=f'p{l["id"]}',horizontal=True)
    if st.button('✓ Жауапты тексеру',key=f'pb{l["id"]}'):
        st.session_state.attempts+=1
        if ans==l['predict_answer']:
            st.session_state.correct+=1;xp(10);st.success('Дұрыс! +10 XP — '+l['predict_explain'])
        else:
            st.error('Қате. Дұрыс жауап: '+l['predict_answer']+' — '+l['predict_explain'])
        save()
    playground();tasks(l);debugging(l);quiz(l)
    s=st.session_state.scores.get(str(l['id']))
    st.markdown('<div class="section-title">📊 Сабақ нәтижесі</div>',unsafe_allow_html=True)
    if s is not None:
        st.progress(s/100)
        cls='ok' if s>=80 else 'info'; msg='келесі тақырыпқа өтуге болады.' if s>=80 else 'тақырыпты қайталау ұсынылады.'
        st.markdown(f'<div class="{cls}">Нәтиже: <b>{s}%</b> — {msg}</div>',unsafe_allow_html=True)
    if st.button('✓ Сабақты аяқтау',type='primary',key=f'complete{l["id"]}'):
        if l['id'] not in st.session_state.completed:
            st.session_state.completed.append(l['id']);xp(20);achievements()
        st.success('Сабақ прогреске қосылды! +20 XP')
        if l['id']<10:
            st.session_state.lesson=l['id']+1;st.rerun()
    a,b=st.columns(2)
    with a:
        if l['id']>1 and st.button('← Алдыңғы сабақ',key=f'prev{l["id"]}'):
            st.session_state.lesson-=1;st.rerun()
    with b:
        if l['id']<10 and l['id'] in st.session_state.completed and st.button('Келесі сабақ →',key=f'next{l["id"]}'):
            st.session_state.lesson+=1;st.rerun()

def lessons():
    st.title('📚 Сабақтар');st.caption('10 негізгі модуль: теория + практика + debugging + mini test.')
    c=st.columns(2)
    for i,l in enumerate(D):
        with c[i%2]:
            card(l);unlocked=l['id']==1 or l['id']-1 in st.session_state.completed
            if st.button('🚀 Ашу' if unlocked else '🔒 Құлыптаулы',key=f'open{l["id"]}',disabled=not unlocked):
                st.session_state.lesson=l['id'];st.session_state.lesson_view=True;st.rerun()
    if st.session_state.lesson_view:
        st.markdown('---');lesson()

def practice():
    st.title('💻 Практика');a,b=st.columns([1.4,.6])
    with a:playground()
    with b:
        st.markdown('<div class="glass"><h3>🔥 Daily Python Challenge</h3><p>1-ден 100-ге дейінгі жұп сандарды шығар.</p><p class="small">+50 XP</p></div>',unsafe_allow_html=True)
        code=st.text_area('Challenge коды',value='for i in range(2,101,2):\n    print(i)',key='daily')
        if st.button('✓ Challenge тексеру',key='daily_check'):
            ok,out=run(code);expected='\n'.join(map(str,range(2,101,2)))
            if ok and out.strip()==expected:
                st.session_state.solved+=1;xp(50);achievements();st.success('🔥 Challenge орындалды! +50 XP')
            else:st.error('Әлі дұрыс емес.')

def errors():
    st.title('🐞 Қатемен жұмыс');st.caption('Жіберілген қателер SQLite ішінде сақталады.')
    if not st.session_state.errors:
        st.markdown('<div class="glass"><h3>✨ Журнал бос</h3><p class="muted">Практикада қате жіберсең, осында пайда болады.</p></div>',unsafe_allow_html=True);return
    for e in reversed(st.session_state.errors):
        st.markdown(f'<div class="glass" style="margin-bottom:12px"><b>🐞 {e["topic"]}</b><div class="small">{e["date"]}</div><p>{e["message"]}</p></div>',unsafe_allow_html=True)

def progress():
    st.title('📊 Менің прогресім');c=st.columns(4)
    for col,args in zip(c,[('📈','Жалпы progress',f'{pct()}%'),('🧩','Шешілген тапсырма',st.session_state.solved),('🐞','Қателер',len(st.session_state.errors)),('⏱️','Оқу уақыты',f'{st.session_state.study_minutes} мин')]):
        with col:stat(*args)
    st.markdown('<div class="section-title">Сабақтар бойынша нәтиже</div>',unsafe_allow_html=True)
    for l in D:
        s=st.session_state.scores.get(str(l['id']),0);st.markdown(f'**{l["icon"]} {l["short"]}** — {s}%');st.progress(s/100)
    weak=[(int(k),v) for k,v in st.session_state.scores.items() if v<80]
    st.markdown('<div class="section-title">🧠 Adaptive Learning</div>',unsafe_allow_html=True)
    if weak:
        for i,s in weak:st.markdown(f'<div class="info">🔄 <b>{D[i-1]["title"]}</b> — {s}%. Қайталау тапсырмалары ұсынылады.</div>',unsafe_allow_html=True)
    else:st.success('✨ 80%-дан төмен нәтиже жоқ.')

def achievements_page():
    st.title('🏆 Жетістіктер');items=[('First Code','🏅','Алғашқы кодты іске қосты.'),('7 Day Streak','🔥','7 күн қатарынан оқыды.'),('Bug Hunter','🐞','10 қате түзету деңгейі.'),('Problem Solver','🧠','20 тапсырма орындады.'),('Final Project','🚀','Қорытынды жобаны аяқтады.')]
    c=st.columns(3)
    for i,(name,icon,desc) in enumerate(items):
        stt='✓ Ашылды' if name in st.session_state.achievements else '🔒 Құлыптаулы'
        with c[i%3]:st.markdown(f'<div class="glass" style="text-align:center;min-height:150px"><div style="font-size:38px">{icon}</div><b>{name}</b><div class="small">{desc}</div><br>{stt}</div>',unsafe_allow_html=True)

def ranking():
    st.title('🏅 Оқушылар рейтингі'); st.caption('Барлық тіркелген оқушылар XP бойынша салыстырылады.')
    c=conn(); rows=c.execute('SELECT name,xp,completed,solved FROM student_progress ORDER BY xp DESC, name ASC').fetchall(); c.close()
    me=st.session_state.student
    data=[{'rank':i+1,'student':r['name'],'xp':r['xp'],'lessons':len(json.loads(r['completed'])),'tasks':r['solved'],'who':'Сен' if r['name']==me else 'Басқалар'} for i,r in enumerate(rows)]
    df=pd.DataFrame(data)
    my=df[df['student']==me].iloc[0]
    st.markdown(f'<div class="info">Сенің орының: <b>{int(my["rank"])}</b> / {len(df)} • ⚡ {int(my["xp"])} XP</div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 XP бойынша диаграмма</div>',unsafe_allow_html=True)
    chart=(alt.Chart(df.head(15)).mark_bar(cornerRadiusTopLeft=6,cornerRadiusTopRight=6)
        .encode(x=alt.X('student:N',sort=alt.EncodingSortField(field='xp',order='descending'),title='Оқушы',axis=alt.Axis(labelAngle=-30)),
                y=alt.Y('xp:Q',title='XP'),
                color=alt.Color('who:N',scale=alt.Scale(domain=['Сен','Басқалар'],range=['#ffd54a','#4da3ff']),legend=alt.Legend(title=None)),
                tooltip=[alt.Tooltip('rank:Q',title='Орын'),alt.Tooltip('student:N',title='Оқушы'),alt.Tooltip('xp:Q',title='XP'),alt.Tooltip('lessons:Q',title='Сабақ'),alt.Tooltip('tasks:Q',title='Тапсырма')])
        .properties(height=380))
    try: st.altair_chart(chart,width='stretch')
    except TypeError: st.altair_chart(chart,use_container_width=True)
    st.markdown('<div class="section-title">🥇 Толық кесте</div>',unsafe_allow_html=True)
    table=df[['rank','student','xp','lessons','tasks']].rename(columns={'rank':'Орын','student':'Оқушы','xp':'XP','lessons':'Сабақ','tasks':'Тапсырма'})
    try: st.dataframe(table,hide_index=True,width='stretch')
    except TypeError: st.dataframe(table,hide_index=True,use_container_width=True)

def final_project():
    st.title('🚀 Final Project');st.markdown('<div class="hero"><div class="eyebrow">CAPSTONE PROJECT</div><h1>🎓 Student Grade Analyzer</h1><p>Аты, бірнеше баға, орташа, max/min және деңгейін анықтайтын бағдарлама жаса.</p></div>',unsafe_allow_html=True)
    for x in ['input — оқушы атын қабылдау','variables — деректерді сақтау','list — бағаларды сақтау','loops — бағаларды өңдеу','if/elif/else — деңгей анықтау','functions — логиканы бөлу','арифметика — орташа баға']:st.markdown('✓ '+x)
    starter='def analyze_student(name, scores):\n    avg = sum(scores) / len(scores)\n    print("Student:", name)\n    print("Average:", avg)\n    print("Max:", max(scores))\n    print("Min:", min(scores))\n    if avg >= 90:\n        print("Level: Excellent")\n    elif avg >= 70:\n        print("Level: Good")\n    else:\n        print("Level: Needs practice")\n\nanalyze_student("Dana", [90,85,95])'
    code=st.text_area('Final Project code',value=starter,height=360)
    if st.button('🚀 Жобаны тексеру',type='primary',key='final_check'):
        ok,out=run(code)
        if ok and 'Dana' in out and ('90.0' in out or '90' in out):
            st.session_state.solved+=1;xp(100);st.session_state.completed=sorted(set(st.session_state.completed+[10]));achievements();st.success('🎉 Final Project негізгі тексеруден өтті! +100 XP');st.code(out)
        else:
            st.error('Жоба толық орындалмаған.');st.code(out)

def about():
    st.title('🔬 Жоба туралы');st.markdown('<div class="hero"><div class="eyebrow">ҒЫЛЫМИ ЖОБА</div><h1>AI көмекшісі</h1><p>Python тілін интерактивті және адаптивті әдістер арқылы оқытудың тиімділігін арттыруға бағытталған заманауи оқу платформасы.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Жоба құрастырушысы</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="glass">👩‍💻 <b>{AUTHOR}</b><div class="small">AI көмекшісі платформасының авторы</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Зерттеу мақсаты</div>',unsafe_allow_html=True);st.markdown('<div class="glass">Python тілін интерактивті және адаптивті әдістер арқылы оқытудың тиімділігін арттыру.</div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Жобаның ерекшеліктері</div>',unsafe_allow_html=True)
    feats=[('📖','Интерактивті теория'),('💻','Код редакторы'),('🧩','Деңгейлік тапсырмалар'),('🐞','Debugging'),('📓','Error Journal'),('📊','Progress Analytics'),('🧠','Adaptive Learning'),('🏆','Gamification'),('👥','Оқушылар рейтингі')]
    c=st.columns(2)
    for i,(ic,n) in enumerate(feats):
        with c[i%2]:st.markdown(f'<div class="glass" style="margin-bottom:12px"><b>{ic} {n}</b><div class="small">Оқу процесін теориядан практикаға байланыстыратын модуль.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="section-title">Практикалық маңызы</div>',unsafe_allow_html=True);st.markdown('<div class="glass">Платформа оқушыны пассивті ақпарат қабылдаудан белсенді код жазуға көшіреді. Теория, кодты болжау, орындау, деңгейлік тапсырма, debugging және mini test бір оқу цикліне біріктірілген. SQLite прогресті сақтауға, ал adaptive learning нәтижеге қарай қайталауды ұсынуға мүмкіндік береді.</div>',unsafe_allow_html=True)

PAGES={'Басты бет':dashboard,'Roadmap':roadmap,'Сабақтар':lessons,'Практика':practice,'Қатемен жұмыс':errors,'Менің прогресім':progress,'Жетістіктер':achievements_page,'Рейтинг':ranking,'Final Project':final_project,'Жоба туралы':about}

def main():
    init_db()
    if not st.session_state.get('student'):
        login_page(); return
    init_state();css();sidebar();p=st.session_state.page
    PAGES.get(p,dashboard)()
    st.markdown('---');st.caption(f'AI көмекшісі • Жоба құрастырушысы: {AUTHOR} • Streamlit + SQLite')

if __name__=='__main__':main()
