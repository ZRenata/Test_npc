import os

def write_doc(date, answer):
    try:
        user = os.getenv("USERPROFILE")
        filename = user + f"\\Desktop\\currencies_{date}.txt"
        file = open(filename, "w", encoding="utf-8")
        file.write(f"Курс валют на дату: {date}" + '\n\n')
        for i in range(len(answer)):
            file.write(f"{answer[i]['Cur_Name']}: {answer[i]['Cur_OfficialRate']}" + '\n')
        file.close()
        return True
    except:
        return False