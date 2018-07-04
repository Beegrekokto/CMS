from django.core.exceptions import ValidationError


# validate image size
def validate_image(image):
    file_size = image.file.size
    limit_kb = 2000
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
