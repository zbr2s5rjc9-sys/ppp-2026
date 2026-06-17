import asyncio
import telegram
import PySimpleGUI as sg

token = 'API_토큰'
chat_id = 8586010059
token = '8685134390:AAFH6P9rD16_nid-98gIrSmk5ILBBbUHHkM'



def watering_advice(temp, humid):

    temp = float(temp)
    humid = float(humid)

    result = ""

    result += "----- 관수 알림 결과 -----\n\n"
    result += f"현재 온도 : {temp:.1f}℃\n"
    result += f"현재 습도 : {humid:.1f}%\n\n"

    if temp >= 25 and humid < 50:

        result += "상태 : 건조 위험\n"
        result += "권장 물주기 : 하루 3회\n"
        result += "권장사항 : 물 공급을 늘리세요."

    elif temp < 20 or humid >= 70:

        result += "상태 : 과습 주의\n"
        result += "권장 물주기 : 하루 1회\n"
        result += "권장사항 : 과도한 관수를 피하세요."

    else:

        result += "상태 : 적정 환경\n"
        result += "권장 물주기 : 하루 2회\n"
        result += "권장사항 : 현재 상태를 유지하세요."

    return result

async def send_message(message):

    bot = telegram.Bot(token=token)

    await bot.send_message(
        chat_id=chat_id,
        text=message
    )


def main():

    layout = [

        [sg.Text("상추 온실 관수 알림 프로그램")],

        [sg.Text("온도(℃)")],
        [sg.Input(key="-TEMP-")],

        [sg.Text("습도(%)")],
        [sg.Input(key="-HUMID-")],

        [sg.Button("관수 판단")],

        [sg.Multiline(size=(50, 12),
                      key="-OUTPUT-")],

        [sg.Button("Exit")]
    ]

    window = sg.Window(
        "상추 온실 관수 알림",
        layout
    )

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        elif event == "관수 판단":

            if (values["-TEMP-"] == "" or
                    values["-HUMID-"] == ""):

                window["-OUTPUT-"].update(
                    "온도와 습도를 모두 입력하세요."
                )

            else:

                try:

                    result = watering_advice(
                        values["-TEMP-"],
                        values["-HUMID-"]
                    )

                    window["-OUTPUT-"].update(result)

                    asyncio.run(send_message(result))

                except:

                    window["-OUTPUT-"].update(
                        "숫자로 입력하세요."
                    )

    window.close()

if __name__ == "__main__":
    main()