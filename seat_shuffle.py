def main():
    # members.txtを開く
    f = open("members.txt", mode="r")

    # 参加者名を読み込む
    name = f.read()

    # 参加者の名前をとりあえず表示させたい
    print(name)

    # ファイルを閉じる
    f.close()

if __name__ == "__main__":
    main()
