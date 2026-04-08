# Write your code here.

#task 1
def hello():
    return f'Hello!'

#task 2
def greet(name):
    return f'Hello, {name}!'

#task3
def calc(a, b, c='multiply'):

    match c:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            try:
                return a * b
            except TypeError:
                return "You can't multiply those values!"
        case 'divide':
            try:
                return a / b
            except ZeroDivisionError:
                return f"You can't divide by 0!"
        case 'modulo':
            return a % b
        case 'int_divide':
            return int(a / b)
        case 'power':
            return a ** b


#task 4
def data_type_conversion(value, type):

    try:
        match type:
            case 'str':
                return str(value)
            case 'int':
                return int(value)
            case 'float':
                return float(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
#task 5
def grade(*args):
    
    try:
        user_grade = (sum(args)/len(args))
    except TypeError:
        return f"Invalid data was provided."

    if user_grade >= 90:
        return 'A'
    elif 89 > user_grade >= 80:
        return 'B'
    elif 79 > user_grade >= 70:
        return 'C'
    elif 69 > user_grade >= 60:
        return 'D'
    else:
        return 'F'
    
#task 6
def repeat(string, count):
    new_string = ''
    for i in range(count):
        new_string += string
    return new_string

#task 7
def student_scores(a, **kwargs):
    if a == 'best':
        high_score = 0
        student_name = ''
        for key, value in kwargs.items():
            if value > high_score:
                high_score = value
                student_name = key
        return student_name      
    elif a == 'mean':
        mean = 0
        for key, value in kwargs.items():
            mean += value

        return mean/len(kwargs)

#task 8
def titleize(s):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = s.split()
    first_word = words[0]
    last_word = words[-1]
    new_words = []

    for word in words:
        if word == first_word or word == last_word:
            word = word.title()
        if word not in little_words:
            word = word.title()
        new_words.append(word)

    new_words = ' '.join(new_words)
            
    return new_words

#task 9
def hangman(a, b):
    guessed = []
    for i in range(len(a)):
        if a[i] in b:
            guessed.append(a[i])
        else:
            guessed.append('_')
            
    return ''.join(guessed)

#task 10
def pig_latin(sentence):
    sentence = sentence.split()
    output = []
    for word in sentence:
        output.append(pig_latin_word(word))
    return ' '.join(output)


def pig_latin_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u' 'qu']

    pre = []
    vowel_index = 0

    if word[0] in vowels:
        return f'{word}ay'
    else:
        for letter in word:
            if letter not in vowels:
                pre.append(letter)
            else:
                vowel_index = word.index(letter)
                break
        return f'{word[vowel_index:]}{"".join(pre)}ay'