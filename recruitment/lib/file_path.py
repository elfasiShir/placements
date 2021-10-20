def user_directory_path(instance, filename=None):
    return f'{instance.user.email}'

def certificate_path(instance, filename):
    base = user_directory_path(instance)
    return f'{base}/certificates/{instance.level}.pdf'

def marksheet_path(instance, filename):
    base = user_directory_path(instance)
    return f'{base}/marksheets/{instance.level}.pdf'

def resume_path(instance, filename):
    base = user_directory_path(instance)
    return f'{base}/resumes/{instance.level}.pdf'

def certifications_path(instance, filename):
    base = user_directory_path(instance)
    # TODO: Check if the below fails for certification name with spaces 
    return f'{base}/certifications/{instance.name + instance.issuing_authority}.pdf'
