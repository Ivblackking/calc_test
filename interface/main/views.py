from django.shortcuts import render
from .models import DefaultNumber, DefaultChecked


def index(request):
    default_salary = DefaultNumber.objects.get(name="salary")
    default_retirement_years = DefaultNumber.objects.get(name="retirement years")
    default_gender = DefaultChecked.objects.get(title_input="gender")
    default_category = DefaultChecked.objects.get(title_input="category")
    default_experience = DefaultNumber.objects.get(name="experience")

    context = {
        "default_salary": default_salary.value,
        "default_retirement_years": default_retirement_years.value,
        "default_gender": default_gender.radio_value,
        "default_category": default_category.radio_value,
        "default_experience": default_experience.value,
    }

    return render(request, 'main/index.html', context=context)
