import csv
from datetime import date
#-----------------------------------------------------
#PARTICIPANT CLASS
class Participant:
    #initialization
    def __init__(self,name:str,idi:int,birth_year:int,birth_month:int,birth_day:int,gender:str):
        self.name = name
        self.idi = idi
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__birth_day = birth_day
        self.__gender = gender

    #methods
    def get_values(self):
        #returning the values as a tuple.
        self.char = {'name': self.name, 'id': self.idi, 'birth_year': self.__birth_year,
                     'birth_month': self.__birth_month, 'birth_day': self.__birth_day, 'gender': self.__gender}
        return tuple(val for val in self.char.values())

    def show_values(self):
        #printing values
        self.char = {'name': self.name, 'id': self.idi, 'birth_year': self.__birth_year,
                     'birth_month': self.__birth_month, 'birth_day': self.__birth_day, 'gender': self.__gender}
        for i,j in self.char.items():
            print(str(i) + ': '+str(j))

    def set_values(self,upd:dict):
        #updating the values according to the input dictionary
        valid = True
        for i in upd:
            if i != 'name' and i!= 'idi' and i!='birth_year' and i!= 'birth_day' and i!='birth_month' and i!= 'gender':
                valid = False
                break
        if valid == True:
            if 'name' in upd:
                self.name = upd['name']
            if 'idi' in upd:
                self.idi = upd['idi']
            if 'birth_year' in upd:
                self.__birth_year = upd['birth_year']
            if 'birth_month' in upd:
                self.__birth_month = upd['birth_month']
            if 'birth_day' in upd:
                self.__birth_day = upd['birth_day']
            if 'gender' in upd:
                self.__gender = upd['gender']
        else:
            return -1

    def calculate_age(self, curr_day: int, curr_month: int, curr_year: int):
        try:
            today = date(curr_year, curr_month, curr_day)
            birthdate = date(self.__birth_year, self.__birth_month, self.__birth_day)
            if today < birthdate:
                return -1
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        except ValueError:
             return -1
#------------------------------------
# STUDENT CLASS
class Student(Participant):
    #initialisation
    def __init__(self,name:str,idi:int,birth_year: int,birth_month: int,birth_day: int,gender: str,grade_level: int,class_assigned: str,gpa: float,selected_activity: str,talent_score: float,athletic_score: float, leadership_score: float ):
        super().__init__(name,idi,birth_year,birth_month,birth_day,gender)
        self.__age = super().calculate_age(1,1,2025)
        self.__grade_level = grade_level
        self.__class_assigned = class_assigned
        self.__gpa = gpa
        self.__selected_activity = selected_activity
        self.__talent_score = talent_score
        self.__athletic_score = athletic_score
        self.__leadership_score = leadership_score
        self.__eligible = False

    def is_eligible(self):
        if self.__gpa >= 5:
            self.__eligible = True
            return True
        else:
            self.__eligible = False
            return False

    def get_values(self):
        return super().get_values() + (self.__age,self.__grade_level,self.__class_assigned,self.__gpa,self.__selected_activity,self.__talent_score,self.__athletic_score,self.__leadership_score,self.__eligible)

    def show_values(self):
        print(self.get_values())
        for i in self.get_values():
            print(i)

    def set_values(self,upd:dict):
        #updating the values according to the input dictionary
        valid = True
        for i in upd:
            if i != 'name' and i != 'idi' and i != 'birth_year' and i != 'birth_day' and i != 'birth_month' and i != 'gender' and i!='grade_level' and i!='class_assigned' and i!='gpa' and i!='selected_activity' and i!='talent_score' and i!='athletic_score' and i!='leadership_score':
                valid = False
                break
        if valid == True:
            upd2 = {}
            if 'name' in upd:
                upd2['name'] = upd['name']
            if 'idi' in upd:
                upd2["idi"] = upd['idi']
            if 'birth_year' in upd:
                upd2["birth_year"] = upd['birth_year']
                self.__age = super().calculate_age(1,1,2025)
            if 'birth_month' in upd:
                upd2["birth_month"] = upd['birth_month']
                self.__age = super().calculate_age(1, 1, 2025)
            if 'birth_day' in upd:
                upd2["birth_day"] = upd['birth_day']
                self.__age = super().calculate_age(1, 1, 2025)
            if 'gender' in upd:
                upd2["gender"] = upd['gender']
            super().set_values(upd2)
            if 'grade_level' in upd:
                self.__grade_level = upd['grade_level']
            if 'class_assigned' in upd:
                self.__class_assigned = upd['class_assigned']
            if 'gpa' in upd:
                self.__gpa = upd['gpa']
                self.is_eligible()
            if 'selected_activity' in upd:
                self.__selected_activity = upd['selected_activity']
            if 'talent_score' in upd:
                self.__talent_score = upd['talent_score']
            if 'athletic_score' in upd:
                self.__athletic_score = upd['athletic_score']
            if 'leadership_score' in upd:
                self.__leadership_score = upd['leadership_score']
        else:
            return -1

#--------------------------------------
#TEACHER CLASS
class Teacher(Participant):
    #initialisation
    def __init__(self,name:str,idi:int,birth_year:int,birth_month:int,birth_day:int,gender:str,subject:str,mentor_grade:int,mentor_class:str,judge:bool):
        super().__init__(name,idi,birth_year,birth_month,birth_day,gender)
        self.__subject = subject
        self.__mentor_grade = mentor_grade
        self.__mentor_class = mentor_class
        self.__judge = judge
    #methods
    def get_values(self):
        return super().get_values() + (self.__subject,self.__mentor_grade,self.__mentor_class,self.__judge)

    def show_values(self):
        for i in self.get_values():
            print(i)

    def set_values(self,upd:dict):
        #updating the values according to the input dictionary
        valid = True
        for i in upd:
            if i != 'name' and i != 'idi' and i != 'birth_year' and i != 'birth_day' and i != 'birth_month' and i != 'gender' and i != 'subject' and i != 'grade_level' and i != 'mentor_class' and i != 'is_eligible':
                valid = False
                break
        if valid == True:
            upd2 = {}
            if 'name' in upd:
                upd2['name'] = upd['name']
            if 'idi' in upd:
                upd2["idi"] = upd['idi']
            if 'birth_year' in upd:
                upd2["birth_year"] = upd['birth_year']
            if 'birth_month' in upd:
                upd2["birth_month"] = upd['birth_month']
            if 'birth_day' in upd:
                upd2["birth_day"] = upd['birth_day']
            if 'gender' in upd:
                upd2["gender"] = upd['gender']
            super().set_values(upd2)
            if 'subject' in upd:
                self.__subject = upd['subject']
            if 'mentor_grade' in upd:
                self.__mentor_grade = upd['mentor_grade']
            if 'mentor_class' in upd:
                self.__mentor_class = upd['mentor_class']
            if 'judge' in upd:
                self.judge = upd['judge']
        else:
            return -1

#---------------------------------------------------------
#---------------------------------------------------------
#ARTIST CLASS
class Artist(Student):
    def __init__(self,name:str,idi:int,birth_year: int,birth_month: int,birth_day: int,gender: str,grade_level: int,class_assigned: str,gpa: float,selected_activity: str,talent_score: float,athletic_score: float, leadership_score: float, talent: str):
        super().__init__(name,idi,birth_year,birth_month,birth_day,gender,grade_level,class_assigned,gpa,selected_activity,talent_score,athletic_score,leadership_score)
        self.__talent = talent
        self.__performance_level = self._Student__talent_score
    #methods
    def get_values(self):
        return super().get_values() + (self.__talent,self.__performance_level)
    def is_eligible(self):
        if self._Student__gpa > 6 and self._Student__age >= 16 :
            self._Student__eligible = True
            return  True
        else:
            self._Student__eligible = False
            return False
    def ret_spec(self):
        return "blackrose"
    def show_values(self):
        for i in self.get_values():
            print(i)
    def compute_scores(self):
        if self.is_eligible() == True:
            return self.__performance_level
        else:
            return -1
    def set_values(self,upd:dict):
        valid = True
        for i in upd:
            if i != 'name' and i != 'idi' and i != 'birth_year' and i != 'birth_day' and i != 'birth_month' and i != 'gender' and i != 'grade_level' and i != 'class_assigned' and i != 'gpa' and i != 'selected_activity' and i != 'talent_score' and i != 'athletic_score' and i != 'leadership_score' and i!= 'talent':
                valid = False
                break
        if valid == True:
            upd2 = {}
            if 'name' in upd:
                upd2['name'] = upd['name']
            if 'idi' in upd:
                upd2["idi"] = upd['idi']
            if 'birth_year' in upd:
                upd2["birth_year"] = upd['birth_year']
            if 'birth_month' in upd:
                upd2["birth_month"] = upd['birth_month']
            if 'birth_day' in upd:
                upd2["birth_day"] = upd['birth_day']
            if 'gender' in upd:
                upd2["gender"] = upd['gender']
            if 'grade_level' in upd:
                upd2["grade_level"] = upd['grade_level']
            if 'class_assigned' in upd:
                upd2["class_assigned"] = upd['class_assigned']
            if 'gpa' in upd:
                upd2["gpa"] = upd['gpa']
                self.is_eligible()
            if 'selected_activity' in upd:
                upd2["selected_activity"] = upd['selected_activity']
            if 'talent_score' in upd:
                upd2["talent_score"] = upd['talent_score']
            if 'athletic_score' in upd:
                upd2["athletic_score"]= upd['athletic_score']
            if 'leadership_score' in upd:
                upd2["leadership_score"] = upd['leadership_score']
            super().set_values(upd2)
            self.__performance_level = self._Student__talent_score
            if 'talent' in upd:
                self.__talent = upd['talent']
        else:
            return -1

#---------------------------------------------------------
#ATHLETE CLASS
class Athlete(Student):
    def __init__(self,name:str,idi:int,birth_year: int,birth_month: int,birth_day: int,gender: str,grade_level: int,class_assigned: str,gpa: float,selected_activity: str,talent_score: float,athletic_score: float, leadership_score: float, sports_category: str,fitness_score:float):
        super().__init__(name,idi,birth_year,birth_month,birth_day,gender,grade_level,class_assigned,gpa,selected_activity,talent_score,athletic_score,leadership_score)
        self.__sports_category = sports_category
        self.__fitness_score = fitness_score
        self.__performance_level = self._Student__athletic_score
    #methods
    def get_values(self):
        return super().get_values() + (self.__sports_category,self.__fitness_score,self.__performance_level)
    def is_eligible(self):
        if self._Student__gpa > 5.5 and self._Student__age >= 12 :
            self._Student__eligible = True
            return  True
        else:
            self._Student__eligible = False
            return False
    def show_values(self):
        for i in self.get_values():
            print(i)
    def compute_scores(self):
        if self.is_eligible() == True:
            return self.__performance_level*self.__fitness_score
        else:
            return -1
    def ret_spec(self):
        return self.__sports_category
    def set_values(self,upd:dict):
        valid = True
        for i in upd:
            if i != 'name' and i != 'idi' and i != 'birth_year' and i != 'birth_day' and i != 'birth_month' and i != 'gender' and i != 'grade_level' and i != 'class_assigned' and i != 'gpa' and i != 'selected_activity' and i != 'talent_score' and i != 'athletic_score' and i != 'leadership_score' and i!= 'fitness_score' and i!='sports_category':
                valid = False
                break
        if valid == True:
            upd2 = {}
            if 'name' in upd:
                upd2['name'] = upd['name']
            if 'idi' in upd:
                upd2["idi"] = upd['idi']
            if 'birth_year' in upd:
                upd2["birth_year"] = upd['birth_year']
            if 'birth_month' in upd:
                upd2["birth_month"] = upd['birth_month']
            if 'birth_day' in upd:
                upd2["birth_day"] = upd['birth_day']
            if 'gender' in upd:
                upd2["gender"] = upd['gender']
            if 'grade_level' in upd:
                upd2["grade_level"] = upd['grade_level']
            if 'class_assigned' in upd:
                upd2["class_assigned"] = upd['class_assigned']
            if 'gpa' in upd:
                upd2["gpa"] = upd['gpa']
                self.is_eligible()
            if 'selected_activity' in upd:
                upd2['selected_activity'] = upd['selected_activity']
            if 'talent_score' in upd:
                upd2['talent_score'] = upd['talent_score']
            if 'athletic_score' in upd:
                upd2["athletic_score"]= upd['athletic_score']
            if 'leadership_score' in upd:
                upd2['leadership_score'] = upd['leadership_score']
            super().set_values(upd2)
            self.__performance_level = self._Student__athletic_score
            if 'sports_category' in upd:
                self.__sports_category = upd['sports_category']
            if 'talent' in upd:
                self.__fitness_score = upd['fitness_score']
        else:
            return -1

#---------------------------------------------------------
#SCHOLAR CLASS
class Scholar(Student):
    def __init__(self,name:str,idi:int,birth_year: int,birth_month: int,birth_day: int,gender: str,grade_level: int,class_assigned: str,gpa: float,selected_activity: str,talent_score: float,athletic_score: float, leadership_score: float, subject_specialization: str,olympiad_scores:list[float]):
        super().__init__(name,idi,birth_year,birth_month,birth_day,gender,grade_level,class_assigned,gpa,selected_activity,talent_score,athletic_score,leadership_score)
        self.__subject_specialization = subject_specialization
        self.__olympiad_scores = olympiad_scores
        self.__performance_level = self._Student__gpa*10
    #methods
    def get_values(self):
        return super().get_values() + (self.__subject_specialization,self.__olympiad_scores,self.__performance_level)
    def is_eligible(self):
        Val = False
        for i in self.__olympiad_scores:
            if i > 80 :
                Val = True
                break

        if self._Student__gpa > 8 and self._Student__age >= 10 and Val == True:
            self._Student__eligible = True
            return  True
        else:
            self._Student__eligible = False
            return False
    def show_values(self):
        for i in self.get_values():
            print(i)
    def compute_scores(self):
        sum = 0
        for i in self.__olympiad_scores:
            sum += i
        if self.is_eligible()==True:
            return self.__performance_level*sum
        else:
            return -1
    def ret_spec(self):
        return self.__subject_specialization
    def set_values(self,upd:dict):
        valid = True
        for i in upd:
            if i != 'name' and i != 'idi' and i != 'birth_year' and i != 'birth_day' and i != 'birth_month' and i != 'gender' and i != 'grade_level' and i != 'class_assigned' and i != 'gpa' and i != 'selected_activity' and i != 'talent_score' and i != 'athletic_score' and i != 'leadership_score' and i!= 'olympiad_scores' and i!='subject_specialization':
                valid = False
                break
        if valid == True:
            upd2 = {}
            if 'name' in upd:
                upd2['name'] = upd['name']
            if 'idi' in upd:
                upd2["idi"] = upd['idi']
            if 'birth_year' in upd:
                upd2["birth_year"] = upd['birth_year']
            if 'birth_month' in upd:
                upd2["birth_month"] = upd['birth_month']
            if 'birth_day' in upd:
                upd2["birth_day"] = upd['birth_day']
            if 'gender' in upd:
                upd2["gender"] = upd['gender']
            if 'grade_level' in upd:
                upd2["grade_level"] = upd['grade_level']
            if 'class_assigned' in upd:
                upd2["class_assigned"] = upd['class_assigned']
            if 'gpa' in upd:
                upd2["gpa"] = upd['gpa']
                self.is_eligible()
            if 'selected_activity' in upd:
                upd2["selected_activity"] = upd['selected_activity']
            if 'talent_score' in upd:
                upd2["talent_score"] = upd['talent_score']
            if 'athletic_score' in upd:
                upd2["athletic_score"]= upd['athletic_score']
            if 'leadership_score' in upd:
                upd2["leadership_score"] = upd['leadership_score']
            super().set_values(upd2)
            self.__performance_level = self._Student__gpa * 10
            if 'subject_specialization' in upd:
                self.__subject_specialization = upd['subject_specialization']
            if 'olympiad_scores' in upd:
                self.__olympiad_scores = upd['olympiad_scores']
        else:
            return -1

#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#ACTIVITY Class
class Activity():
    def __init__(self,activity_id: int, activity_name: str,activity_type: str, max_participants: int,grade_level: int,is_active: bool,participants : list[Participant], organizers : list[Teacher]):
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.__activity_type = activity_type
        self.__max_participants = max_participants
        self.__grade_level = grade_level
        self.__is_active = is_active
        self.__participants = participants
        self.__organizers = organizers

    def get_values(self):
        return (self.activity_name,self.activity_id,self.__activity_type,self.__max_participants,self.__grade_level,self.__is_active) + tuple(i.name for i in self.__participants) + tuple(i.name for i in self.__organizers)
    def show_values(self):
        for i in self.get_values():
            print(i)
    def set_values(self,upd:dict):
        valid = True
        for i in upd:
            if i != 'activity_id' and i != 'activity_name' and i != 'activity_type' and i != 'max_participants' and i != 'grade_level' and i != 'is_active' and i != 'participants' and i != 'organizers':
                valid = False
                break
        if valid == True:
            if 'activity_id' in upd:
                self.activity_id= upd['activity_id']
            if 'activity_name' in upd:
                self.activity_name = upd['activity_name']
            if 'activity_type' in upd:
                self.activity_type = upd['activity_type']
            if 'max_participants' in upd:
                self.__max_participants = upd['max_participants']
            if 'grade_level' in upd:
                self.__grade_level = upd['grade_level']
            if 'is_active' in upd:
                self.__is_active = upd['is_active']
            if 'participants' in upd:
                self.__participants = upd['participants']
            if 'organizers' in upd:
                self.__organizers = upd['organizers']
        else:
            return -1

#-------------------------------
#SPORTSTOURNAMENT Class
class SportsTournament(Activity):
    def __init__(self,activity_id: int, activity_name: str,activity_type: str, max_participants: int,grade_level: int,is_active: bool,participants : list[Athlete], organizers : list[Teacher],game_type: str,duration_minutes: int):
        super().__init__(activity_id,activity_name,activity_type,max_participants,grade_level,is_active,participants,organizers)
        self.__game_type = game_type
        self.__duration_minutes = duration_minutes
    def show_values(self):
        super().show_values()
        print(self.__game_type)
        print(self.__duration_minutes)
    def determine_winnerr(self):
        if self.__game_type == 'Team':
            classes = {}
            for i in self._Activity__participants:
                if i._Student__class_assigned not in classes:
                    classes[i._Student__class_assigned] = [i]
                else:
                    classes[i._Student__class_assigned] += [i]
            max = 0
            max1 = -1
            for i in classes:
                score = 0
                for j in classes[i]:
                    score += j.compute_scores()
                score = score/len(classes[i])
                if score > max:
                    max = score
                    max1 = i

            return max1
        elif self.__game_type == 'Individual' :
            max = 0
            max1 = -1
            for i in self._Activity__participants:
                if i.compute_scores() > max:
                    max = i.compute_scores()
                    max1 = i
            return max1
        else:
            return -1
    def determine_winner(self):
        if self.__game_type == 'Team':
            classes = {}
            for i in self._Activity__participants:
                if i._Student__class_assigned not in classes:
                    classes[i._Student__class_assigned] = [i]
                else:
                    classes[i._Student__class_assigned] += [i]
            max = 0
            max1 = -1
            for i in classes:
                score = 0
                for j in classes[i]:
                    score += j.compute_scores()
                score = score/len(classes[i])
                if score > max:
                    max = score
                    max1 = i
            highp = 0
            maxp = -1
            for i in classes[max1]:
                if i.compute_scores() > highp:
                    highp = i.compute_scores()
                    maxp = i

            return  maxp
        elif self.__game_type == 'Individual' :
            max = 0
            max1 = -1
            for i in self._Activity__participants:
                if i.compute_scores() > max:
                    max = i.compute_scores()
                    max1 = i
            return max1
        else:
            return -1
#-------------------------------
#TALENTSHOW Class
class TalentShow(Activity):
    def __init__(self,activity_id: int, activity_name: str,activity_type: str, max_participants: int,grade_level: int,is_active: bool,participants : list[Artist], organizers : list[Teacher],talent_categories: list):
        super().__init__(activity_id,activity_name,activity_type,max_participants,grade_level,is_active,participants,organizers)
        self.__talent_categories = talent_categories
    def show_values(self):
        super().show_values()
        print(self.__talent_categories)
    def evaluate_talent(self):
        max = 0
        max1 = -1
        for i in self._Activity__participants:
            if i.compute_scores() > max:
                max = i.compute_scores()
                max1 = i
        return max1
    def determine_winnerr(self):
        max = 0
        max1 = -1
        for i in self._Activity__participants:
            if i.compute_scores() > max:
                max = i.compute_scores()
                max1 = i
        return max1
#-------------------------------
#ACADEMICCOMPETITION Class
class AcademicCompetition(Activity):
    def __init__(self,activity_id: int, activity_name: str,activity_type: str, max_participants: int,grade_level: int,is_active: bool,participants : list[Scholar], organizers : list[Teacher],subjects: list,max_marks:float):
        super().__init__(activity_id,activity_name,activity_type,max_participants,grade_level,is_active,participants,organizers)
        self.__subjects = subjects
        self.__max_marks = max_marks
    def show_values(self):
        super().show_values()
        print(self.__subjects)
        print(self.__max_marks)
    def determine_winner(self):
        max = 0
        max1 = -1
        for i in self._Activity__participants:
            if i.compute_scores() > max:
                max = i.compute_scores()
                max1 = i
        return max1
    def determine_winnerr(self):
        max = 0
        max1 = -1
        for i in self._Activity__participants:
            if i.compute_scores() > max:
                max = i.compute_scores()
                max1 = i
        return max1

#-----------------------------------------------------
#Defining functions to read files
#reading part data
def load_participant_data(filepath:str):
    stds = []
    teach = []
    with open(filepath,'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        (data[0][0], data[0][1],data[0][6], data[0][7], data[0][8], data[0][9], data[0][10], data[0][11], data[0][12]) = (
        data[0][1], data[0][0], data[0][12], data[0][10], data[0][9], data[0][11], data[0][8], data[0][6],
         data[0][7] )
        type = {1:str,2:int,3:int,4:int,5:int,6:str,7:int,8:str,9:float,10:str,11:float,12:float,13:float}
        type2 = {1:str,2:int,3:int,4:int,5:int,6:str,19:str,20:int,21:str,22:bool}
        for i in range(1,len(data)):
            (data[i][0], data[i][1], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11],data[i][12]) = (data[i][1], data[i][0], data[i][12], data[i][10], data[i][9], data[i][11], data[i][8], data[i][6],data[i][7])
            if data[i][18:22] == ['','','','']:
                for j in type:
                    data[i][j - 1] = type[j](data[i][j - 1])

                stds.append(Student(**{data[0][k]:data[i][k] for k in range(13)}))

            else:
                for j in type2:
                    if j == 22:
                        if data[i][j - 1] == 'FALSE':
                            data[i][j - 1] = False
                        else:
                            data[i][j - 1] = True
                    else:
                        data[i][j - 1] = type2[j](data[i][j - 1])

                teach.append(Teacher(**({data[0][k]:data[i][k] for k in range(6)}|{data[0][k]:data[i][k] for k in range(18,22)})))
    return stds,teach

#activities...
def load_activities_data(filepath:str):
    sportst = []
    talentwa = []
    acadcomp = []
    with open(filepath,'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        type = {1:int,4:int,5:int,7:int}
        type2 = {1:int,4:int,5:int}
        type3 = {1:int,4:int,5:int,10:float}
        for i in range(1,len(data)):
            if data[i][5] != "":
                for j in type:
                    data[i][j - 1] = type[j](data[i][j - 1])
                sportst.append(SportsTournament(**({data[0][k]:data[i][k] for k in range(5)}|{"is_active":False,"participants":[],"organizers":[]}|{data[0][5]:data[i][5],data[0][6]:data[i][6]})))
            elif data[i][7] != "":
                data[i][7] = data[i][7].replace('-',' ')
                data[i][7] = data[i][7].split()
                for j in type2:
                    data[i][j - 1] = type2[j](data[i][j - 1])
                talentwa.append(TalentShow(**(
                            {data[0][k]: data[i][k] for k in range(5)} | {"is_active": False, "participants": [],
                                                                          "organizers": []}|{data[0][7]:data[i][7]})))
            else:
                for j in type3:
                    data[i][j - 1] = type3[j](data[i][j - 1])
                acadcomp.append(AcademicCompetition(**({data[0][k]: data[i][k] for k in range(5)} | {"is_active": False, "participants": [],
                                                             "organizers": []}|{data[0][8]:[data[i][8]],data[0][9]:data[i][9]})))
        return sportst, talentwa, acadcomp

#-----------------------------------------------
#Specialised Participant Data Analysis
#sort into artists,athlete,scholars
def specialised_students(filepath:str):
    with open(filepath,'r') as file:
        artists = {}
        arts = []
        athletes = {}
        athl = []
        scholars = {}
        schls = []
        reader = csv.reader(file)
        data = [row for row in reader]
        (data[0][0], data[0][1],data[0][6], data[0][7], data[0][8], data[0][9], data[0][10], data[0][11], data[0][12],data[0][14],data[0][15]) = (
        data[0][1], data[0][0], data[0][12], data[0][10], data[0][9], data[0][11], data[0][8], data[0][6],
        data[0][7],data[0][15],data[0][14] )
        type1 = {1:str,2:int,3:int,4:int,5:int,6:str,7:int,8:str,9:float,10:str,11:float,12:float,13:float,14:str}
        type2 = {1:str,2:int,3:int,4:int,5:int,6:str,7:int,8:str,9:float,10:str,11:float,12:float,13:float,15:str}
        type3 = {1:str,2:int,3:int,4:int,5:int,6:str,7:int,8:str,9:float,10:str,11:float,12:float,13:float,17:float}
        for i in range(1,len(data)):
            (data[i][0], data[i][1], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11],data[i][12],data[i][14],data[i][15]) = (data[i][1], data[i][0], data[i][12], data[i][10], data[i][9], data[i][11], data[i][8], data[i][6],data[i][7],data[i][15],data[i][14])
            if data[i][18:22] == ['', '', '', '']:
                if data[i][13] != "":
                    for j in type1:
                        data[i][j - 1] = type1[j](data[i][j - 1])
                    arts.append(Artist(**{data[0][k]: data[i][k] for k in range(14)}))
                    if data[i][7] not in artists:
                        artists[data[i][7]] = [Artist(**{data[0][k]: data[i][k] for k in range(14)})]
                    else:
                        artists[data[i][7]] += [Artist(**{data[0][k]: data[i][k] for k in range(14)})]
                elif data[i][14] != "":
                    for j in type2:
                        data[i][j - 1] = type2[j](data[i][j - 1])
                    b = (data[i][15]).replace('-', ' ')
                    data[i][15] = b.split()
                    trial = data[i][15][0:len(data[i][15])]
                    data[i][15] = [float(ll) for ll in trial]

                    schls.append(Scholar(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][14]: data[i][14],
                                                                                              data[0][15]: data[i][
                                                                                                  15]})))
                    if data[i][7] not in scholars:
                        scholars[data[i][7]] = [Scholar(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][14]: data[i][14],
                                                                                              data[0][15]: data[i][
                                                                                                  15]}))]
                    else:
                        scholars[data[i][7]] += [Scholar(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][15]: data[i][15],data[0][14]: data[i][14]}))]

                else:
                    for j in type3:
                        data[i][j - 1] = type3[j](data[i][j - 1])

                    athl.append(Athlete(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][16]: data[i][16],
                                                                                              data[0][17]: data[i][
                                                                                                  17]})))
                    if data[i][7] not in athletes:
                        athletes[data[i][7]] = [Athlete(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][16]: data[i][16],
                                                                                              data[0][17]: data[i][
                                                                                                  17]}))]
                    else:
                        athletes[data[i][7]] += [Athlete(**({data[0][k]: data[i][k] for k in range(13)} | {data[0][16]: data[i][16],
                                                                                              data[0][17]: data[i][
                                                                                                      17]}))]

    #writing the respective csvs.
    for i in artists:
        with open(i+"-artist.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(["participant_id","name","grade_level","class_assigned","score"])
            for j in artists[i]:
                writer.writerow([j.idi, j.name, int(i[0:len(i)-1]), i, j.compute_scores()])
    for i in athletes:
        with open(i+"-athlete.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(["participant_id","name","grade_level","class_assigned","score"])
            for j in athletes[i]:
                writer.writerow([j.idi, j.name, int(i[0:len(i)-1]), i, j.compute_scores()])
    for i in scholars:
        with open(i+"-scholar.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(["participant_id","name","grade_level","class_assigned","score"])
            for j in scholars[i]:
                writer.writerow([j.idi, j.name, int(i[0:len(i)-1]), i, j.compute_scores()])


    return arts,athl,schls
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def register_activity(participant_filepath: str, activity_filepath: str):
    content = load_activities_data(activity_filepath)
    master = [{},{},{}]
    #dividing activities acc to grade and sports,talentshw and academiccomp
    for j in range(3):
        for i in content[j]:
            if i._Activity__grade_level not in master[j]:
                master[j][i._Activity__grade_level] = {i.activity_name:i}
            else:
                master[j][i._Activity__grade_level].update({i.activity_name:i})
    #sorting eligible students acc to grade
    stds2 = specialised_students(participant_filepath)
    stds = (stds2[1],stds2[0],stds2[2])
    masterstud = [{},{},{}]
    for i in range(len(stds)):
        for j in stds[i]:
            if (j.is_eligible() == True) and (j._Student__grade_level not in masterstud[i]):
                masterstud[i][j._Student__grade_level] = [j]
            elif (j.is_eligible() == True):
                masterstud[i][j._Student__grade_level] += [j]
    stdunnec,teach = load_participant_data(participant_filepath)
    #classify teachers according to their grade only if they're judges
    teachr = {}
    for i in teach:
        if i._Teacher__judge == True and i._Teacher__mentor_grade not in teachr:
            teachr[i._Teacher__mentor_grade] = [i]
        elif i._Teacher__judge == True:
            teachr[i._Teacher__mentor_grade] += [i]
    #final rendition
    for i in range(len(master)):
        for j in master[i]:
            if j in teachr:
               for k in master[i][j]:
                   master[i][j][k].set_values({'organizers': teachr[j]})
    for i in range(len(masterstud)):
        for j in masterstud[i]:
            #students in a grade classified according to the activity
            #classf is for a grade {activityname : [artist]} mapping
            classf = {}
            #print(masterstud[i][j])
            for k in masterstud[i][j]:
                if k.ret_spec() not in classf:
                    classf[k.ret_spec()] = [k]
                else:
                    classf[k.ret_spec()] += [k]
            for k in classf:
                if k in master[i][j]:
                    master[i][j][k].set_values({'participants': classf[k]})
                #checking if active/not
                if classf[k] == 'cricket':
                    kakshas = []
                    for m in classf[0]:
                        if m._Student__class_assigned not in kakshas:
                            kakshas.append(m._Student__class_assigned)
                    if len(kakshas) >= 2 and (len(classf[k]) <= master[i][j][k]._Activity__max_participants) and \
                            master[i][j][k]._Activity__organizers != []:
                        master[i][j][k].set_values({'is_active': True})
                else:
                    if len(classf[k]) >= 2 and (len(classf[k]) <= master[i][j][k]._Activity__max_participants) and \
                            master[i][j][k]._Activity__organizers != []:
                        master[i][j][k].set_values({'is_active': True})

    return [master[0][k]['cricket'] for k in range(6,13)],[master[0][k]['chess'] for k in range(6,13)],[master[2][k]['mathematics'] for k in range(6,13)],[master[2][k]['science'] for k in range(6,13)],[master[2][k]['computers'] for k in range(6,13)],[master[1][k]['blackrose'] for k in range(6,13)]
####-----------------------------------------------####
#Finding Winner
def winners(activities:()):
    loser = {i : [] for i in range(6,13)}
    for i in activities:
        for j in i:
            loser[j._Activity__grade_level] += [j]
    for i in loser:
        with open('grade'+str(i)+'.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(['cricket','chess','mathematics','science','computers','blackrose'])
            results = []
            for j in loser[i]:
                if (j._Activity__participants != []) and (j._Activity__is_active == True):
                        results.append(j.determine_winnerr())
                else:
                    results.append('NA')
            writer.writerow(results)


'''winners(register_activity('easy_participant_data.csv','easy_activity_data.csv'))'''

"""register_activity('easy_participant_data.csv','easy_activity_data.csv')"""
'''a,b,c,d,e,f = register_activity('easy_participant_data.csv','easy_activity_data.csv')
for i in a:
    print(i)'''


'''print(specialised_students("easy_participant_data.csv"))'''