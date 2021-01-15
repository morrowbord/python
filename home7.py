import json

with open("text777.json", "w", encoding="utf-8") as write_file:
    with open("text_7.txt", "r", encoding="utf-8") as t3_file:
        everage_profit = 0
        final_result = {}
        i = 0
        for content in t3_file:
            profit = int(content.split()[2])-int(content.split()[3])
            if profit > 0:
                everage_profit = everage_profit + profit
                i += 1
                ev = (everage_profit) / i
                ev = str(ev)

            result = {content.split()[0]: profit}
            final_result = {**final_result,**result}

            # result = тут надо взять значения словаря и сделать один
            print(result)
        final_result = [final_result,ev]
        json.dump(final_result, write_file, ensure_ascii=False, indent=4)