# Student performance fixer

This project is a collection of functions for fixing student's performance in E-Diary system.

## Features
- Get Schoolkid object by it's full name
- Fix marks that are less than 4 out of 5
- Remove chastisements
- Create commendation of random phrase for specified subject

## Setup
1. Download `fix.py`
```bash
curl https://github.com/gennadis/e-diary/blob/master/fix.py  --output fix.py
```

2. Place it in a E-diary system folder, where the `manage.py` file is located

3. Open Django shell
```bash
python manage.py shell
```

4. Import `fix.py` in Django shell
```python
import fix
```                        

## Examples
1. To init, create a Schoolkid object
```python
student = get_schoolkid('Your Name')
```

2. To fix student's marks that are less than `4` points, use
```python
fix_marks(student)
```

3. To remove student's chastisements, run
```python
remove_chastisements(student)
```


4. To create a commendation of random phrase for specified subject, run
```python
create_commendation(student, 'Subject Title')
```
