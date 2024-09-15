import random

class CovidSymptom:
    def __init__(self, fever, cold, shivering, weight_loss, cough, headache, fatigue, sore_throat, breathlessness, chest_pain, loss_of_taste_smell):
        self.fever = fever
        self.cold = cold
        self.shivering = shivering
        self.weight_loss = weight_loss
        self.cough = cough
        self.headache = headache
        self.fatigue = fatigue
        self.sore_throat = sore_throat
        self.breathlessness = breathlessness
        self.chest_pain = chest_pain
        self.loss_of_taste_smell = loss_of_taste_smell

    def __repr__(self):
        return (f"Fever: {self.fever}, Cold: {self.cold}, Shivering: {self.shivering}, Weight Loss: {self.weight_loss}, "
                f"Cough: {self.cough}, Headache: {self.headache}, Fatigue: {self.fatigue}, "
                f"Sore Throat: {self.sore_throat}, Breathlessness: {self.breathlessness}, "
                f"Chest Pain: {self.chest_pain}, Loss of Taste/Smell: {self.loss_of_taste_smell}")

def generate_random_symptoms():
    data = []
    for _ in range(100):
        fever = random.randint(97, 104)  # Random temperature in Fahrenheit
        cold = random.randint(0, 3)          # Cold severity from 0 to 3
        shivering = random.randint(0, 3)     # Shivering severity from 0 to 3
        weight_loss = random.uniform(0, 10)  # Weight loss in kg
        cough = random.randint(0, 3)         # Cough severity from 0 to 3
        headache = random.randint(0, 3)      # Headache severity from 0 to 3
        fatigue = random.randint(0, 3)       # Fatigue severity from 0 to 3
        sore_throat = random.randint(0, 3)   # Sore throat severity from 0 to 3
        breathlessness = random.randint(0, 3)  # Breathlessness severity from 0 to 3
        chest_pain = random.randint(0, 3)      # Chest pain severity from 0 to 3
        loss_of_taste_smell = random.randint(0, 3)  # Loss of taste/smell severity from 0 to 3
        
        data.append(CovidSymptom(fever, cold, shivering, weight_loss, cough, headache, fatigue, sore_throat, breathlessness, chest_pain, loss_of_taste_smell))
    return data

def sort_by_parameter(data, parameter):
    param_map = {
        "fever": lambda x: x.fever,
        "cold": lambda x: x.cold,
        "shivering": lambda x: x.shivering,
        "weight_loss": lambda x: x.weight_loss,
        "cough": lambda x: x.cough,
        "headache": lambda x: x.headache,
        "fatigue": lambda x: x.fatigue,
        "sore_throat": lambda x: x.sore_throat,
        "breathlessness": lambda x: x.breathlessness,
        "chest_pain": lambda x: x.chest_pain,
        "loss_of_taste_smell": lambda x: x.loss_of_taste_smell
    }

    if parameter in param_map:
        return sorted(data, key=param_map[parameter])
    else:
        raise ValueError(f"Unknown parameter: {parameter}")


covid_data = generate_random_symptoms()
sort_param = input("Enter the parameter to sort by: ")
sorted_data = sort_by_parameter(covid_data, sort_param)
for i in sorted_data:
    print(i)
