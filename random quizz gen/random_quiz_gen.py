#Project from page 235 of Automate the boring stuff with python

import random

statesCapitals = {}

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoenix', 'Arkansas': 'Little Rock', 'California':'Sacramento', 'Colorado':'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise','Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines','Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge','Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston','Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln','Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton','New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



for quiz_num in range(35):
	#Create all the files for the quizs and the answers
	with open(f'quiz {quiz_num}.txt\n\n', 'w', encoding='utf-8') as quiz_file:
		quiz_file.write(f"Quiz No {quiz_num}")
		
	with open(f'answers {quiz_num}.txt', 'w', encoding='utf-8') as answers_file:
		answers_file.write(f"Answers No {quiz_num}\n\n")
	
	#Shuffle all the states to randomize the order and get one question for each state
	states = list(capitals.keys())
	random.shuffle(states)
	
	for state in states:
		question = f'What is the capital of {state}?\n\n'
		propositions = []
		if random.randint(1,2) == 1:
			
			propositions.append(f'{capitals[state]}\n')
			states.remove(state)
			propositions.append(f'{capitals[states[random.randint(0,len(states)-1)]]}\n\n')
		else:
			states.remove(state)
			propositions.append(f'{capitals[states[random.randint(0,len(states)-1)]]}\n\n')
			propositions.append(f'{capitals[state]}\n')
			
		with open(f'quiz {quiz_num}.txt', 'a', encoding='utf-8') as quiz_file:
			quiz_file.write(question + propositions[0] + propositions[1])
		
		with open(f'answers {quiz_num}.txt', 'a', encoding='utf-8') as answers_file:
			answers_file.write(question + f'{capitals[state]}\n\n')
	
		
	
	
	
	
	
	
	
	
