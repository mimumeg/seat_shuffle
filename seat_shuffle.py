import random

def main():
    # members.txtを開く
    with open("members.txt", mode="r") as f:
        members_text = f.read()

        # 参加者の情報を一つ一つ取得したいため、リスト化する
        members_list = members_text.split("\n")

    # 参加者の名前をとりあえず表示させたい
    print(members_list)


if __name__ == "__main__":
    main()