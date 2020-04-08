import streamlit as st
import webbrowser as wb
import numpy as np
from datetime import datetime
import math
import pandas as pd
from PIL import Image

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Candidate:
	def __init__(self, name, adress, town, state, zip_code, phone, email = [], linkedin = [], github = [], twitter = []):
		self.name = name
		self.adress = adress
		self.town = town
		self.state = state
		self.zip = str(zip_code)
		self.phone = phone
		self.email = email
		self.linkedin = linkedin
		self.github = github
		self.twitter = twitter
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Company(Candidate):
	def __init__(self, title, industry, begin_employ, end_employ, name, adress, town, state, zip_code, phone, supervisor):
		super().__init__(name, adress, town, state, zip_code, phone)
		self.title = title
		self.industry = industry
		self.begin = begin_employ
		self.end = end_employ
		self.supervisor = supervisor
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Reference:
	def __init__(self, name, company, title, relationship, years_known, email):
		self.name = name
		self.company = company
		self.title = title
		self.relationship = relationship
		self.years_known = years_known
		self.email = email
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

class Education:
	def __init__(self, instituation, begin, end=[], town=[], state=[], degree=[], minor = [], concentration = []):
		self.instituation = instituation
		self.begin = begin
		self.end = end
		self.town = town
		self.state = state
		self.degree = degree
		self.minor = minor
		self.concentration = concentration
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

references_list = [Reference('Dr. Ben Cook', 'University of Wyoming', 'Director of UW MBA Program', 'Current Supervisor', '2', 'bencook@uwyo.edu'), 
				Reference('Kyle Tynsky', 'Saulsbury Industries', 'Sr. Director of Supply Chain & Procurement', 'Former Supervisor', '5+', 'ktynsky@saulsbury.com'),
				Reference('Larry Weatherfod', 'University of Wyoming', 'Scarlett Chair and Professor of Decision Science', 'Professor will earning my MBA', '2', 'lrw@uwyo.edu'),
				Reference('Sean Sullivan', 'Elkhorn Construction', 'CEO (Retired)', 'Work for Sean during 2 summer internships', '6+', 'ssullivan@eheci.com')]

previous_employers = [Company('Graduate Research Assistant', 'Higher Education', 'August 2018', 'Currect', 'University of Wyoming', '1000 E University Ave', 'Laramie', 'Wyoming', 82071, '(307) 766-112', 'Dr. Ben Cook'),
						Company('Cost Estimator / Field Engineer', 'Heavy Industrial Construction', 'May 2017', 'June 2018','Saulsbury Industries', '3010 Lyndon B Johnson Fwy #1100', 'Dallas', 'Texas', 75234, '(972) 884-6000', 'Kyle Tynsky')]

job_responsibilities = {previous_employers[0].name: ['Python Web Application I Built: https://carbon-safe.herokuapp.com/',
													'Assisted in constructing a techno-economic model that analyzes the feasibility of using Amine Gas Treatment to capture CO2 at coal fired power plants around Wyoming.',
													'We modeled the CAPEX of the various facilities that are required for the technology, the various avenues where the captured CO2 could go (injected into the ground for tax credits and/or sold to oil fields for enhanced oil recovery), the estimated OPEX for each year, and the complex post closure monitoring costs and long-term liability costs.',
													'Our work is a critical step in evaluating the business case for Amine capture technology, supporting the State of Wyoming’s CarbonSAFE initiative, and most importantly, hopefully helping save Wyoming jobs at these coal fired power plants around the state.',
													'Re-built our Excel model into a Python web application. This was being done for three reasons: 1) Allow all stakeholders easy access to the model, 2) Reduce the human error that occurs with a complex Excel model, 3) Give me an opportunity to further develop my Python and development skills.',
													'CarbonSAFE Phase II Information: https://www.uwyo.edu/cegr/research-projects/carbonsafe-p2-dryfork.html'],
						previous_employers[1].name: ['Lead Estimator for various heavy industrial construction projects ranging from $100K to $50MM. Support mechanical estimator for similar type projects upwards of $150MM.',
													'Research and fully understand the scope of the proposal, divide and assign work to support estimators, coordinate with proposals department and client to address questions throughout the estimator process, and obtain then review offers and quotes for subcontractors or vendors.'
													'Review all work in completed estimate, perform risk analysis, and Monte Carlo simulations on high risk estimates.',
													'Personally present the prepared estimate to stakeholders (Director of Estimating, Project Manager(s), and other executives depending on the size and inherent risk in the project).',
													"Temporary Field Engineer for one of SI’s struggling projects. I was sent to a site in Oklahoma to personally help the project manager better track the project’s spent manhours and earned hours (Earned Value Management).",
													'I performed an audit of what was currently being done to track spent and earned hours, identified various potential causes for the problems the project was seeing, and helped implement changes that led to more accurate project tacking.Completed a week-long course on best practices for Project Management taught be executives from Saulsbury.']}

schools_list = [Education('University of Wyoming', 'August 2018', 'May 2020', 'Laramie', 'Wyoming', 'Master of Business Administration (MBA)', concentration = 'Energy Management'),
				Education('Colorado School of Mines', 'August 2013', 'May 2017', 'Golden', 'Colorado', 'B.S. in Mechanical Engineering', minor = 'Economics'),
				Education('Udemy', 'January 2020', degree = 'Data Science Bootcamp')]

if len(previous_employers) != len(job_responsibilities):
	raise ValueError('Number of Employers (' + str(len(previous_employers)) + ') does not match number of Responsibilities (' + str(len(job_responsibilities)) + ')')

user = Candidate('Brayton J. Sanders', '1080 North 18th Street', 'Laramie', 'Wyoming', 82072, '(307) 679-8244', 'brayton5473@gmail.com',
					'https://www.linkedin.com/in/bsanders5473/', 'https://github.com/BraytonJSanders', 'https://twitter.com/BraytonJSanders')

profile = "I am a young individual that brings a diverse skillset, a desire for success, and a passion for and a pride in what I do. I’m seeking a Data Science or Data Analyst position to begin after the completion of my MBA come late May. I can start as soon as June 1st. I have 2 years of experience using Python. Most of which is from building personal and exploratory machine learning web applications with Streamlit. I also have some development background from my current Research Assistant position. I am looking for positions in the Salt Lake City area or Wyoming"

skills = {'Languages':
					[{'Python':
							['Jupyter Notebook, Sublime Text', 'Streamlit (What I made this resume with)', 'NumPy, pandas, matplolib, etc.']},
					'R', 'VBA', 'MATLAB'],
		'Data Science':
					[{'Machine Learning':
							['scikit-learn', 'TensorFlow']},
					'Data Visualization', 'Statistics', 'Ability to conduct research and gather qualitative data'],
		'Business': 
					[{'All Microsoft Office products':
													['Highly advanced in Excel']},
					{'Business Analyst':
															['SWAT, PESTAL, BMC, etc']},
					'Project evaluation, financial and economic Excel modeling', 'Implementing open innovation and intrapreneur techniques', 'Ability to perform market research and develop a business marketing plan', 'Financial accounting, managerial accounting, and cost estimating'],
		'Engineering':
					['Ability to solve complex problems', 'Computational Fluid Dynamics', 'Designing Mechanical Systems', 'SolidWorks, AutoCAD, and Arduino'],
		'Other Skills':
					['Ability and willingness to learn new software applications', 'Technical writing, formal presentations, quick learner, and very detail oriented', 'Strong ability to work independently as well as collaboratively/a team lead']}
personal_interests = ['Cooking and Creating New Recipes', 'Health and Fitness', 'Sports & Athletics (Favorite: Wrestling)', 'Learning New Things, Being Curious',
							'Bow Hunting Elk', 'Fly & Ice Fishing']
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def show_skills(skills):
	st.write('________')
	st.title('Skills and Knowledge'); st.text('')
	for subject in skills:
		st.header('*' + subject + '*')
		for skill in skills[subject]:
			if type(skill) == type({'Key': 'Dummy'}):
				st.subheader(list(skill.keys())[0])
				for sub_skill in skill[list(skill.keys())[0]]:
					st.text(sub_skill)
			else:
				st.subheader(skill)
		st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def show_personal(interests):
	st.write('________')
	st.header('Personal Interests'); st.subheader('')
	for interest in interests:
		st.write(interest)
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def employment_history(companies_info, responsibilities):
	st.write('________')
	st.header('Employment History'); st.text('')
	for i in previous_employers:
		st.subheader(i.name)
		st.text(i.industry)
		st.text(i.begin + ' to ' + i.end)
		st.text(i.town + ', ' + i.state)
		st.write(i.title)

		if st.checkbox('Responsibilities' + ' at ' + i.name):
			for duty in responsibilities[i.name]:
				st.write(duty)
			st.write('________')
			st.write('________')

		if st.checkbox(i.name + ' Contact Information'):
			st.text(i.adress)
			st.text(i.town + ', ' + i.state); st.text('')
			st.text(i.phone)
			st.text('Supervisor: ' + i.supervisor)
			st.write('________')

		if companies_info.index(i) != len(companies_info)-1:
			st.title('')
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def contact_info():
	st.write(user.adress)
	st.write(user.town + ', ' + user.state + ' ' + user.zip); st.text(' ')
	st.write(user.phone); st.text(' ')
	st.write(user.email)

	if st.button('- LinkedIn'):
		wb.open(user.linkedin, new = 0, autoraise = True)
		st.text('If button fails to launch new tab: '+ user.linkedin)

	if st.button('- GitHub'):
		wb.open(user.github, new = 0, autoraise = True)
		st.text('If button fails to launch new tab: '+ user.github)

	if st.button('- Twitter'):
		wb.open(user.twitter, new = 0, autoraise = True)
		st.text('If button fails to launch new tab: '+ user.twitter)
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

@st.cache
def life_timeline_df(current):
	time_frame = []
	for month in np.arange(2009.0 + (8/12), current + (1/12), (1/12)):
		month_i = str(int(round((month % 1)*12)))
		year_i = str(month)[:4] if str(month)[5:7] != '99' else str(int(str(month)[:4])+1)
		time_frame.append(datetime.strptime(month_i + ' ' + year_i, '%m %Y').strftime('%B %Y'))

	what_doing = pd.DataFrame(np.zeros((len(time_frame), 2)), index = [time_frame], columns = ['What Doing', 'Picture'])

	what_doing.iloc[:3, 0] = 'Attending Evanston (WY) High School - Freshman (In Football Season)'
	what_doing.iloc[3:7, 0] = 'Attending Evanston (WY) High School - Freshman (In Wrestling Season)'
	what_doing.iloc[7:10, 0] = 'Attending Evanston (WY) High School - Freshman (In Track & Baseball Season)'
	what_doing.iloc[10:12, 0] = 'Survey for Cook-Sanders Associates (In Baseball Season)'
	what_doing.iloc[:10, 1] = 'pics/EHS.png'
	what_doing.iloc[3:7, 1] = 'pics/wrestling2.jpg'
	what_doing.iloc[10:12, 1] = 'pics/survey.jpg'

	what_doing.iloc[12:15, 0] = 'Attending Evanston (WY) High School - Sophmore (In Football Season)'
	what_doing.iloc[15:19, 0] = 'Attending Evanston (WY) High School - Sophmore (In Wrestling Season)'
	what_doing.iloc[19:22, 0] = 'Attending Evanston (WY) High School - Sophmore (In Track & Baseball Season)'
	what_doing.iloc[22:24, 0] = 'Survey for Cook-Sanders Associates (In Baseball Season)'
	what_doing.iloc[12:22, 1] = 'pics/EHS.png'
	what_doing.iloc[22:24, 1] = 'pics/survey.jpg'

	what_doing.iloc[24:27, 0] = 'Attending Evanston (WY) High School - Junior (In Football Season)'
	what_doing.iloc[27:31, 0] = 'Attending Evanston (WY) High School - Junior (In Wrestling Season)'
	what_doing.iloc[31:34, 0] = 'Attending Evanston (WY) High School - Junior (In Track & Baseball Season)'
	what_doing.iloc[34:36, 0] = 'Survey for Cook-Sanders Associates (In Baseball Season)'
	what_doing.iloc[24:34, 1] = 'pics/EHS.png'
	what_doing.iloc[27:31, 1] = 'pics/champ.jpeg'
	what_doing.iloc[31:34, 1] = 'pics/EHS.png'
	what_doing.iloc[34:36, 1] = 'pics/survey.jpg'

	what_doing.iloc[36:39, 0] = 'Attending Evanston (WY) High School - Senior (In Football Season)'
	what_doing.iloc[39:43, 0] = 'Attending Evanston (WY) High School - Senior (In Wrestling Season)'
	what_doing.iloc[43:45, 0] = 'Attending Evanston (WY) High School - Senior (In Track & Baseball Season)'
	what_doing.iloc[45, 0] = 'Graduated from Evanston High School'
	what_doing.iloc[46:48, 0] = 'Survey Crew Chief for Cook-Sanders Associates (In Baseball Season)'
	what_doing.iloc[36:46, 1] = 'pics/EHS.png'
	what_doing.iloc[39:43, 1] = 'pics/wrestling1.jpg'
	what_doing.iloc[46:48, 1] = 'pics/survey.jpg'

	what_doing.iloc[48:52, 0] = 'Attending Colorado School of Mines - Freshman (In Football Season)'
	what_doing.iloc[52:58, 0] = 'Attending Colorado School of Mines - Freshman'
	what_doing.iloc[58:60, 0] = 'Cost Estimating Intern at Elkhorn Construction - Evanston, WY'
	what_doing.iloc[48:58, 1] = 'pics/CSM.png'
	what_doing.iloc[58:60, 1] = 'pics/wood.png'
	
	what_doing.iloc[60:70, 0] = 'Attending Colorado School of Mines - Sophmore'
	what_doing.iloc[70:72, 0] = 'Mechanical Engineer intern at Chevron - Salt Lake City, UT'
	what_doing.iloc[60:70, 1] = 'pics/CSM.png'
	what_doing.iloc[70:72, 1] = 'pics/chevron.png'

	what_doing.iloc[72:75, 0] = 'Attending Colorado School of Mines - Junior'
	what_doing.iloc[75:78, 0] = 'Attending Colorado School of Mines - Junior (Rugby Season)'
	what_doing.iloc[78:82, 0] = 'Attending Colorado School of Mines - Junior'
	what_doing.iloc[82:84, 0] = 'Mechanical Engineer intern at Wood Group - Denver, CO'
	what_doing.iloc[72:82, 1] = 'pics/CSM.png'
	what_doing.iloc[75:78, 1] = 'pics/rugby2.jpg'
	what_doing.iloc[81, 1] = 'pics/mines1.jpg'
	what_doing.iloc[82:84, 1] = 'pics/wood.png'

	what_doing.iloc[84:87, 0] = 'Attending Colorado School of Mines - Senior'
	what_doing.iloc[87:90, 0] = 'Attending Colorado School of Mines - Senior (Rugby Season)'
	what_doing.iloc[90:93, 0] = 'Attending Colorado School of Mines - Senior'
	what_doing.iloc[93, 0] = 'Graduated from Colorado School of Mines - B.S. in Mechanical Engineering, Minor in Economics'
	what_doing.iloc[84:92, 1] = 'pics/CSM.png'
	what_doing.iloc[87:90, 1] = 'pics/rugby1.jpg'

	what_doing.iloc[92, 1] = 'pics/sr_design.jpeg'
	what_doing.iloc[93, 1] = 'pics/csm_grad.jpg'

	what_doing.iloc[94:102, 0] = 'Cost Estimator for Saulsbury Industries'
	what_doing.iloc[102:105, 0] = 'Field Engineer for Saulsbury Industries'
	what_doing.iloc[105:107, 0] = 'Cost Estimator for Saulsbury Industries'
	what_doing.iloc[94:107, 1] = 'pics/SI.jpg'


	what_doing.iloc[107:108, 0] = 'Mechanical Engineer for Cook-Sanders Associates'
	what_doing.iloc[107:108, 1] = 'pics/csa.jpg'

	what_doing.iloc[108:118, 0] = 'Attending the University of Wyoming'
	what_doing.iloc[118:120, 0] = 'Summer MBA Project for Black Hills Energy'
	what_doing.iloc[120:, 0] = 'Attending the University of Wyoming'
	what_doing.iloc[108:, 1] = 'pics/UW.png'
	what_doing.iloc[108:110, 1] = 'pics/UW4.jpeg'
	what_doing.iloc[110:112, 1] = 'pics/UW3.jpeg'
	what_doing.iloc[122, 1] = 'pics/UW5.jpeg'
	what_doing.iloc[112:114, 1] = 'pics/UW6.jpeg'
	what_doing.iloc[120:122, 1] = 'pics/UW1.jpg'
	what_doing.iloc[123:125, 1] = 'pics/UW2.jpeg'
	what_doing.iloc[-2:, 1] = 'pics/gf.jpeg'
	return what_doing
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def life_timeline():
	current = float(datetime.today().year) + float(datetime.today().month)/12

	time = st.slider("Life Timeline:", 2009.0 + (8/12), current, current, (1/12))

	select_month = str(round((time % 1)*12))
	select_year = str(time)[:4] if str(time)[5:7] != '99' else str(int(str(time)[:4])+1)

	selection = datetime.strptime(select_month + ' ' + select_year, '%m %Y').strftime('%B %Y')
	timeline = life_timeline_df(current)
	# st.dataframe(timeline)

	st.subheader(selection)
	st.write(timeline['What Doing'][selection][0])
	st.image(Image.open(timeline['Picture'][selection][0]))
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def show_references(references):
	for ref in references:
		st.subheader(ref.name)
		st.write(ref.company)
		st.text(ref.title)
		st.text('Relationship: ' + ref.relationship)
		st.text('Years Known: ' + ref.years_known)
		st.write('Email: ' + ref.email)

		if references.index(ref) != len(references)-1:
			st.text('')

	st.subheader("Contact me for reference's phone numbers")
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def show_education(schools):
	st.write('________')
	st.header('Education'); st.text('')
	for school in schools:
		st.subheader(school.instituation)

		if len(school.end) > 0:
			st.text(school.begin + ' to ' + school.end)
		else:
			st.text(school.begin)

		if len(school.town) > 0:
			st.text(school.town + ', ' + school.state)

		st.write(school.degree)

		if len(school.minor) > 0:
			st.write('Minor:  ' + school.minor)
		if len(school.concentration) > 0:
			st.write('Concentration:  ' + school.concentration)

		if schools.index(school) != len(schools)-1:
			st.subheader('')
	st.write('________')
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def sign_off():
	st.title(''); st.title(''); st.title('')
	st.text('Created by: Brayton Sanders')
	st.text(datetime.today().strftime('%A - %B %d, %Y'))
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# headshot.jpeg
def main():
	st.write('________')
	st.title(user.name); st.text('')
	st.write('Data Science - Data Analitics')
	st.text('Engineer-In-Training (EIT)')
	st.text('MBA, Mechanical Engineering, Economics'); st.subheader('')
	st.image(Image.open('pics/headshot.jpeg'))
	st.write('________'); st.write('________')

	st.subheader('Profile:')
	st.write(profile)
	st.write('Please browse the sections below. Enjoy!')


	st.write('________'); st.write('________')

	if st.checkbox('Contact Information'):
		contact_info()

	if st.checkbox('View Education'):
		show_education(schools_list)

	if st.checkbox('View Employment History'):
		employment_history(previous_employers, job_responsibilities)

	if st.checkbox('View My References'):
		show_references(references_list)

	if st.checkbox('View Life Timeline'):
		life_timeline()

	if st.checkbox('View Skills and Knowledge'):
		show_skills(skills)
	if st.checkbox('View personal Interests'):
		show_personal(personal_interests)
	st.write('________')

	sign_off()

	

	




# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
	main()





