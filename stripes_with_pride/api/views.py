from django.shortcuts import render, redirect

from api.models import Score

# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def dyslexia_modes(request):
    return render(request, 'dyslexia_modes.html', {'title': 'Dyslexia'})

def dyslexia_visual(request):
    return render(request, 'dyslexia_visual.html', {'title': 'Dyslexia Visual'})

def dyslexia_auditory(request):
    return render(request, 'dyslexia_auditory.html', {'title': 'Dyslexia Auditory'})

def referrals(request):
    return render(request, 'referrals.html', {'title': 'Referrals'})

def assessment(request):
    assessment_dict = {
        "q1": {
            "questiontext":"Do you confuse visually similar words such as cat and cot?",
            "options": {
     	        "Rarely": "3",
                "Occasionally": "6",
                "Often": "9",
     	        "Most of the time": "12"
            }
        },
        "q2": {
            "questiontext":"Do you lose your place or miss out lines when reading?",
            "options": {
                "Rarely": "2",
                "Occasionally": "4",
                "Often": "6",
                "Most of the time": "8"
            }
        },
        "q3": {
            "questiontext":"Do you confuse the names of objects, for example table for chair?",
            "options": {
     	        "Rarely": "1",
     	        "Occasionally": "2",
     	        "Often": "3",
     	        "Most of the time": "4"
     	    }
        },
        "q4": {
            "questiontext":"Do you have trouble telling left from right?",
            "options":{
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
            }
        },
        "q5": {
            "questiontext":"Is map reading or finding your way to a strange place confusing?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
     	    }
        },
        "q6": {
            "questiontext":"Do you re-read paragraphs to understand them?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
     	        }
        },
        "q7": {
            "questiontext":"Do you get confused when given several instructions at once?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
     	    }
        },
        "q8": {
            "questiontext":"Do you make mistakes when taking down telephone messages?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
            }
        },
        "q9": {
            "questiontext":"Do you find it difficult to find the right word to say?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
     	    }
        },
        "q10": {
            "questiontext":"How often do you think of creative solutions to problems?",
            "options": {
                "Rarely": "1",
                "Occasionally": "2",
                "Often": "3",
                "Most of the time": "4"
            }
        },
        "q11": {
            "questiontext":"How easy do you find it to sound out words such as e-le-phant?",
            "options": {
                "Easy": "3",
                "Challenging": "6",
                "Difficult": "9",
                "Very Difficult": "12"
     	    }
        },
        "q12": {
            "questiontext":"When writing, do you find it difficult to organise thoughts on paper?",
            "options": {
                "Easy": "2",
                "Challenging": "4",
                "Difficult": "6",
                "Very Difficult": "8"
     	    }
        },
        "q13": {
            "questiontext":"Did you learn your multiplication tables easily?",
            "options": {
                "Easy": "2",
                "Challenging": "4",
                "Difficult": "6",
                "Very Difficult": "8"
     	    }
        },
        "q14": {
            "questiontext":"How easy do you find it to recite the alphabet?",
            "options": {
     	        "Easy": "1",
                "Challenging": "2",
                "Difficult": "3",
                "Very Difficult": "4"
     	    }
        },
        "q15": {
            "questiontext":"How hard do you find it to read aloud?",
            "options": {
                "Easy": "1",
                "Challenging": "2",
                "Difficult": "3",
                "Very Difficult": "4"
            }
        }
    }

    return render(request, 'assessment.html', {'title': 'Assessment', 'questions': assessment_dict})

def results(request, uuid):
    score = Score.objects.get(uuid=uuid).score
    if score < 45:
        return redirect(request, 'results.html', {'title': 'Results', 'result': 'You may have a low level of dyslexia'})
    elif score < 60:
        return render(request, 'results.html', {'title': 'Results', 'result': 'You may have a moderate level of dyslexia'})
    else:
        return render(request, 'results.html', {'title': 'Results', 'result': 'You may have a high level of dyslexia'})

def scoring(request):
    if request.method == 'POST':
        data = request.POST
        # score = sum([v for k, v in data.items()])
        submission = Score.objects.create(assessment='dyslexia', score=50)
        return redirect('results', uuid=submission.uuid)

def email(request, uuid):
    submission = Score.objects.get(uuid=uuid)
    return render(request, 'email.html', {'title': 'Email'})
