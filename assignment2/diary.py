import traceback

diary_input = ''
special_line = 'done for now'

with open('diary.txt', 'a')as file:
    try:
        prompt = 1
        while diary_input != special_line:
            if prompt == 1:
                diary_input = input('What happened today? ')
            elif prompt == 0:
                diary_input = input('What else? ')
            prompt = 0
            file.write(f'{diary_input}\n')
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")