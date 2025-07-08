import random
import pyttsx3
engine = pyttsx3.init()   #iss module se pc bolta hai
 
questions = [
    {"question": "Who is known as the Father of the Nation in India?", "options": ["A) Mahatma Gandhi","B) Jawaharlal Nehru","C) Sardar Patel","D) Bhagat Singh"], "answer":"A"},
    {"question": "What is the national currency of India?", "options": ["A) Dollar","B) Rupee","C) Euro","D) Yen"], "answer":"B"},
    {"question": "Which city is known as the 'Pink City'?", "options": ["A) Delhi","B) Jaipur","C) Mumbai","D) Kolkata"], "answer":"B"},
    {"question": "Who was the first President of India?", "options": ["A) Rajendra Prasad","B) APJ Abdul Kalam","C) S Radhakrishnan","D) Lal Bahadur Shastri"], "answer":"A"},
    {"question": "What is the national animal of India?", "options": ["A) Lion","B) Tiger","C) Elephant","D) Leopard"], "answer":"B"},
    {"question": "How many states does India have (as of 2024)?", "options": ["A) 28","B) 29","C) 30","D) 31"], "answer":"A"},
    {"question": "Which Indian river is called the 'Ganga of the South'?", "options": ["A) Godavari","B) Yamuna","C) Krishna","D) Kaveri"], "answer":"A"},
    {"question": "What is the national bird of India?", "options": ["A) Peacock","B) Sparrow","C) Parrot","D) Crow"], "answer":"A"},
    {"question": "Which festival is known as the 'Festival of Lights'?", "options": ["A) Holi","B) Diwali","C) Eid","D) Baisakhi"], "answer":"B"},
    {"question": "Which is the smallest state of India by area?", "options": ["A) Sikkim","B) Goa","C) Tripura","D) Manipur"], "answer":"B"},
    {"question": "Who wrote India's national anthem 'Jana Gana Mana'?", "options": ["A) Bankim Chandra Chatterjee","B) Rabindranath Tagore","C) Subhash Chandra Bose","D) Sarojini Naidu"], "answer":"B"},
    {"question": "Which planet is known as the 'Red Planet'?", "options": ["A) Earth","B) Mars","C) Jupiter","D) Venus"], "answer":"B"},
    {"question": "Who was the first woman Prime Minister of India?", "options": ["A) Indira Gandhi","B) Pratibha Patil","C) Sonia Gandhi","D) Sarojini Naidu"], "answer":"A"},
    {"question": "Which monument is called the 'Symbol of Love'?", "options": ["A) India Gate","B) Qutub Minar","C) Taj Mahal","D) Charminar"], "answer":"C"},
    {"question": "What is the national sport of India?", "options": ["A) Cricket","B) Hockey","C) Football","D) Kabaddi"], "answer":"B"},
    {"question": "Who invented the number system with 'Zero'?", "options": ["A) Aryabhata","B) Newton","C) Einstein","D) Galileo"], "answer":"A"},
    {"question": "Which Indian state is famous for tea plantations?", "options": ["A) Kerala","B) Assam","C) Gujarat","D) Punjab"], "answer":"B"},
    {"question": "Which city is called the 'Silicon Valley of India'?", "options": ["A) Hyderabad","B) Mumbai","C) Bengaluru","D) Pune"], "answer":"C"},
    {"question": "Who is called the 'Iron Man of India'?", "options": ["A) Mahatma Gandhi","B) Jawaharlal Nehru","C) Sardar Vallabhbhai Patel","D) Subhash Chandra Bose"], "answer":"C"},
    {"question": "What is the capital of India?", "options": ["A) Mumbai","B) New Delhi","C) Chennai","D) Kolkata"], "answer":"B"},
    {"question": "Which ocean lies to the south of India?", "options": ["A) Atlantic","B) Arctic","C) Indian Ocean","D) Pacific"], "answer":"C"},
    {"question": "Who gave the slogan 'Quit India'?", "options": ["A) Mahatma Gandhi","B) Jawaharlal Nehru","C) Bhagat Singh","D) Subhash Chandra Bose"], "answer":"A"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["A) Oxygen","B) Nitrogen","C) Carbon Dioxide","D) Hydrogen"], "answer":"C"},
    {"question": "Where is the Sun Temple located?", "options": ["A) Odisha","B) Rajasthan","C) Gujarat","D) Tamil Nadu"], "answer":"A"},
    {"question": "What is the national flower of India?", "options": ["A) Rose","B) Sunflower","C) Lotus","D) Marigold"], "answer":"C"},
    {"question": "Who is the current Prime Minister of India?", "options": ["A) Narendra Modi","B) Manmohan Singh","C) Atal Bihari Vajpayee","D) Inder Kumar Gujral"], "answer":"A"},
    {"question": "Which mountain range forms the northern boundary of India?", "options": ["A) Himalayas","B) Andes","C) Alps","D) Rockies"], "answer":"A"},
    {"question": "What is the full form of ISRO?", "options": ["A) Indian Space Research Organisation","B) Indian Science Research Organization","C) International Space Research Organisation","D) Indian Space Robo Org"], "answer":"A"},
    {"question": "Which state is called the 'Land of Five Rivers'?", "options": ["A) Punjab","B) Haryana","C) Uttar Pradesh","D) Rajasthan"], "answer":"A"},
    {"question": "Where is the Gateway of India located?", "options": ["A) Delhi","B) Mumbai","C) Kolkata","D) Chennai"], "answer":"B"},
    {"question": "Which dance form originates from Tamil Nadu?", "options": ["A) Kathak","B) Bharatanatyam","C) Kuchipudi","D) Odissi"], "answer":"B"},
    {"question": "Which festival features a water fight in India?", "options": ["A) Baisakhi","B) Ganesh Chaturthi","C) Holi","D) Diwali"], "answer":"C"},
    {"question": "Which is the highest mountain peak in India?", "options": ["A) Kangchenjunga","B) Everest","C) K2","D) Nanda Devi"], "answer":"A"},
    {"question": "Who was the first Indian woman to win an Olympic medal?", "options": ["A) P.T. Usha","B) Mary Kom","C) Karnam Malleswari","D) Saina Nehwal"], "answer":"A"},
    {"question": "Which city is called the 'City of Joy'?", "options": ["A) Mumbai","B) Kolkata","C) Chennai","D) Bengaluru"], "answer":"B"},
    {"question": "Which Indian state has the largest population?", "options": ["A) Uttar Pradesh","B) Maharashtra","C) Bihar","D) West Bengal"], "answer":"A"},
    {"question": "Which river is called the 'Sorrow of Bihar'?", "options": ["A) Ganga","B) Kosi","C) Yamuna","D) Brahmaputra"], "answer":"B"},
    {"question": "Which freedom fighter wrote the poem 'Give me blood and I will give you freedom'?", "options": ["A) Subhash Chandra Bose","B) Bhagat Singh","C) Chandra Shekhar Azad","D) Bal Gangadhar Tilak"], "answer":"A"},
    {"question": "Which wildlife sanctuary is known for one-horned rhinoceros?", "options": ["A) Kaziranga","B) Gir","C) Ranthambore","D) Sundarbans"], "answer":"A"},
    {"question": "Which Indian state is famous for its backwaters?", "options": ["A) Goa","B) Kerala","C) West Bengal","D) Odisha"], "answer":"B"},
    {"question": "Which part of India is the Thar Desert located in?", "options": ["A) Gujarat & Rajasthan","B) Punjab","C) Haryana","D) Uttar Pradesh"], "answer":"A"},
    {"question": "What is the capital of Tamil Nadu?", "options": ["A) Chennai","B) Bengaluru","C) Hyderabad","D) Kochi"], "answer":"A"},
    {"question": "Who is the 'Missile Man of India'?", "options": ["A) Vikram Sarabhai","B) A.P.J. Abdul Kalam","C) Satish Dhawan","D) Rakesh Sharma"], "answer":"B"},
    {"question": "Which Indian day is celebrated on January 26?", "options": ["A) Independence Day","B) Republic Day","C) Gandhi Jayanti","D) Children's Day"], "answer":"B"},
    {"question": "Which monument is a memorial to the victims of Jallianwala Bagh massacre?", "options": ["A) Jantar Mantar","B) Jallianwala Bagh Memorial","C) India Gate","D) Parliament House"], "answer":"B"},
    {"question": "Which Indian city is known as the 'Manchester of India'?", "options": ["A) Mumbai","B) Ahmedabad","C) Pune","D) Coimbatore"], "answer":"B"},
    {"question": "Which is India's national aquatic animal?", "options": ["A) Dolphin","B) Whale","C) Shark","D) Otter"], "answer":"A"},
    {"question": "Which island group is part of India?", "options": ["A) Maldives","B) Sri Lanka","C) Lakshadweep","D) Seychelles"], "answer":"C"},
    {"question": "Which national park is known for Bengal tigers?", "options": ["A) Jim Corbett","B) Gir","C) Kaziranga","D) Bandipur"], "answer":"A"},
    {"question": "What is the name of India's first satellite?", "options": ["A) Chandrayaan-1","B) Aryabhata","C) Rohini","D) Mangalyaan"], "answer":"B"},
    {"question": "Which Indian festival celebrates the harvest season in Punjab?", "options": ["A) Onam","B) Baisakhi","C) Pongal","D) Lohri"], "answer":"B"},
    {"question": "Which is the Prime Meridian passing through India?", "options": ["A) 82.5°E","B) 77°E","C) 85°E","D) 90°E"], "answer":"A"},
    {"question": "Which lake is famous in Srinagar, Kashmir?", "options": ["A) Dal Lake","B) Wular Lake","C) Chilika Lake","D) Vembanad Lake"], "answer":"A"},
    {"question": "What is the sacred scripture of Sikhism?", "options": ["A) Guru Granth Sahib","B) Vedas","C) Quran","D) Bible"], "answer":"A"},
    {"question": "Who is the Hindi cinema actor known as 'King Khan'?", "options": ["A) Salman Khan","B) Aamir Khan","C) Shah Rukh Khan","D) Hrithik Roshan"], "answer":"C"},
    {"question": "Which state is the headquarters of ISRO?", "options": ["A) Maharashtra","B) Karnataka","C) Andhra Pradesh","D) Telangana"], "answer":"B"},
    {"question": "Which temple is known as the 'Golden Temple'?", "options": ["A) Jagannath Temple","B) Meenakshi Temple","C) Golden Temple","D) Kedarnath Temple"], "answer":"C"},
    {"question": "Which Indian city hosts the annual literary festival 'Taj Mahotsav'?", "options": ["A) Agra","B) Delhi","C) Jaipur","D) Chennai"], "answer":"A"},
    {"question": "Which award is the highest civilian honour in India?", "options": ["A) Padma Shri","B) Padma Bhushan","C) Padma Vibhushan","D) Bharat Ratna"], "answer":"D"},
    {"question": "Which Indian state is called the 'Land of the Rising Sun'?", "options": ["A) Arunachal Pradesh","B) Manipur","C) Assam","D) Nagaland"], "answer":"A"},
    {"question": "Which Indian dance originates from Odisha?", "options": ["A) Bharatanatyam","B) Kathak","C) Odissi","D) Kathakali"], "answer":"C"},
    {"question": "What is the capital of Assam?", "options": ["A) Dispur","B) Guwahati","C) Shillong","D) Imphal"], "answer":"A"},
    {"question": "Which Indian cricketer scored 100 international centuries?", "options": ["A) Sachin Tendulkar","B) Ricky Ponting","C) Virat Kohli","D) Brian Lara"], "answer":"A"},
    {"question": "Which mountain pass connects India to Afghanistan?", "options": ["A) Khyber Pass","B) Rohtang Pass","C) Zoji La","D) Nathula Pass"], "answer":"A"},
    {"question": "Which Indian fruit is the national fruit?", "options": ["A) Mango","B) Banana","C) Apple","D) Orange"], "answer":"A"},
    {"question": "What is the literacy day observed in India?", "options": ["A) 8th September","B) 15th August","C) 14th November","D) 1st April"], "answer":"A"},
    {"question": "Which festival in Kerala involves boat races?", "options": ["A) Onam","B) Baisakhi","C) Pongal","D) Holi"], "answer":"A"},
    {"question": "Which Indian state has the most coastline?", "options": ["A) Gujarat","B) Tamil Nadu","C) Andhra Pradesh","D) Kerala"], "answer":"A"},
    {"question": "Which wildlife reserve is famous for Asiatic lions?", "options": ["A) Gir National Park","B) Ranthambore","C) Kaziranga","D) Corbett"], "answer":"A"},
    {"question": "Which group makes up India's Parliament?", "options": ["A) Lok Sabha","B) Rajya Sabha","C) Both Lok & Rajya Sabha","D) Supreme Court"], "answer":"C"},
    {"question": "Which festival involves decorating with lights and lamps in West Bengal?", "options": ["A) Durga Puja","B) Diwali","C) Pongal","D) Onam"], "answer":"A"},
    {"question": "Which Indian city is known for automobile manufacturing (Tata Motors)?", "options": ["A) Pune","B) Jamshedpur","C) Chennai","D) Noida"], "answer":"B"},
    {"question": "Where is the Indian Institute of Technology (IIT) founded first?", "options": ["A) Mumbai","B) Delhi","C) Kharagpur","D) Chennai"], "answer":"C"},
    {"question": "Which Indian scientist is known for the theory of Raman Effect?", "options": ["A) C.V. Raman","B) A.P.J. Abdul Kalam","C) Vikram Sarabhai","D) Satyendra Nath Bose"], "answer":"A"},
    {"question": "Which is the highest civilian award for women in India?", "options": ["A) Arjuna Award","B) Khel Ratna","C) Padma Shri","D) Bharat Ratna"], "answer":"C"},
    {"question": "Which metal is India the world's second largest producer of?", "options": ["A) Iron","B) Steel","C) Aluminum","D) Copper"], "answer":"B"},
    {"question": "Which Indian city is famous for its diamond industry?", "options": ["A) Surat","B) Vadodara","C) Hyderabad","D) Jaipur"], "answer":"A"}
    # Total 100 questions
]


def speak(thing):
    engine.say(thing)
    engine.runAndWait()

name = input("What is your name?")
print(f"Welcome {name}! Let's Begin Kaun Banegaaaa Crorepati ")
speak(f"Welcome {name} Let's Begin Kaun Banegaaa Crorepati ")
prize = 0

for i in questions:
    random_question = (random.choice(questions))
    # print(random_question)
    que = random_question.get("question")
    opt = random_question.get("options")
    ans = random_question.get("answer")

    print("\n" + que)
    for option in opt:
        print(option)

    inp = input("Enter The Option Which u will Select : ")
    input_answer = inp.upper()

    if(input_answer == ans):
        prize += 100000
        print("Correct Answer!")
        print(f"You won {prize} Dollars")
        speak(f"You won {prize} Dollars")

    else:
        print("Better Luck Next Time!")
        speak("Better Luck Next Time!")  
        break    

print(f"Congratulations! {name} you won {prize} Dollars")
speak(f"Congratulations! {name} you won {prize} Dollars")

