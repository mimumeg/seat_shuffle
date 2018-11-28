import random

def main():
    # members.txtを開く
    with open("members.txt", mode="r") as f:
        members_text = f.read()

        # 参加者の情報を一つ一つ取得したいため、リスト化する
        members_list = members_text.split("\n")

    # テーブルを３つ作成
    table1 = []
    table2 = []
    table3 = []

    # 人数の分だけ繰り返すようにカウンターを作成
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # デーブル1：6人分シャッフルするまで終了しない
    while counter1 < 6:
        # 参加者を1人シャッフル選出
        results = random.choice(members_list)

        # table1に格納
        table1.append(results)

        # 参加者リストから取り出した氏名を削除
        members_list.remove(results);

        # カウンターに1足す
        counter1 += 1

        # print(f"テーブル1：{table1}")
        # print(members_list)

        # デーブル2：5人分シャッフルするまで終了しない
        while counter2 < 5:
            # 参加者を1人シャッフル選出
            results = random.choice(members_list)

            # table1に格納
            table2.append(results)

            # 参加者リストから取り出した氏名を削除
            members_list.remove(results);

            # カウンターに1足す
            counter2 += 1

            # print(f"テーブル2：{table2}")
            # print(members_list)

            # デーブル3：4人分シャッフルするまで終了しない
            while counter3 < 4:
                # 参加者を1人シャッフル選出
                results = random.choice(members_list)

                # table1に格納
                table3.append(results)

                # 参加者リストから取り出した氏名を削除
                members_list.remove(results)

                # カウンターに1足す
                counter3 += 1

    # リスト化を解除
    final_results1 = ", ".join(table1)
    final_results2 = ", ".join(table2)
    final_results3 = ", ".join(table3)

    # シャッフル結果を表示。
    print(f"--------席替えアプリ--------")
    print(f"テーブル1：{final_results1}")
    print(f"テーブル2：{final_results2}")
    print(f"テーブル3：{final_results3}")

if __name__ == "__main__":
    main()