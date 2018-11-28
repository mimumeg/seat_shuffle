import random

def main():
    # members.txtを開く
    with open("members.txt", mode="r") as f:
        members_text = f.read()

        # 参加者の情報を一つ一つ取得したいため、リスト化する
        members_list = members_text.split("\n")

    # 参加者の名前をとりあえず表示させたい
    # print(members_list)

    # テーブルを３つ作成
    table1 = []
    table2 = []
    table3 = []

    # 15人分シャッフルするまで終了しない

    # 参加者を1人シャッフル選出
    results = random.choice(members_list)

    # table1に格納
    table1.append(results)

    # 参加者リストから取り出した氏名を削除
    members_list.remove(results);

    print(table1)
    print(members_list)


if __name__ == "__main__":
    main()