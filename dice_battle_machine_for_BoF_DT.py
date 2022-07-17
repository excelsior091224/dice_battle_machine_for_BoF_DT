import random, os, time
from datetime import datetime

# ダイスのクラス
class Dice:
    def __init__(self, dice_num, dice_size):
        # ダイスの数
        self.num = dice_num
        # ダイスの面数
        self.size = dice_size
    
    # ダイスを投げたときの処理
    def throw_dice(self):
        # ダイスの目を格納するリスト
        dice_roll = []
        # ダイスの数だけ繰り返すループ
        for i in range(self.num):
            # ダイスの面数からランダムな数（ダイスの出目）を変数numに代入
            num = random.randint(1, self.size)
            # ダイスの出目numをリストdice_rollに格納
            dice_roll.append(num)
        # ダイスの目が個数分入ったリストを返り値とする
        # 例：6面ダイス2個の場合：[1個目のダイスの目,2個目のダイスの目]
        return dice_roll

# ボクサーのクラス
class Boxer:
    def __init__(self, corner, name, punch_power, speed, toughness, dice_12, dice_6):
        # ボクサーのコーナー（赤or青）
        self.corner = corner
        # ボクサーの名前
        self.name = name
        # HPの数
        self.hp = 40
        # パンチ力
        self.punch_power = punch_power
        # スピード
        self.speed = speed
        # タフネス
        self.toughness = toughness
        # 12面ダイス2個
        self.dice_12 = dice_12
        # 6面ダイス2個
        self.dice_6 = dice_6
        # 1ラウンドごとの攻勢に回った回数
        self.attack_num = 0
        # 試合結果
        self.result = ''
        print(self.name + '\n' + 'HP:' + str(self.hp) + '\n' + 'パンチ力:' + str(self.punch_power) + '\n' + 'スピード:' + str(self.speed) + '\n' + 'タフネス:' + str(self.toughness))

# 対戦ログを保存するフォルダを作成する関数
def make_folder():
    fight_log_dir = "fight_log"
    try:
        os.makedirs(fight_log_dir)
    except FileExistsError:
        pass
    return fight_log_dir

# 数値入力関数
# num_typeには入力する数値の種別を入れる
def decide_num(num_type):
    # 変数numが決定されるまでループ
    while True:
        # 1以上の数値を入力
        num = input('{}の値を入力してください（1以上の数字）:'.format(num_type))
        # 入力値を整数に変換
        try:
            num = int(num)
        # 数字以外の文字が入力された場合
        except ValueError:
            print("数字を入力してください")
        # 数字が入力された場合
        else:
            # 数字が0以下（0及び負の整数）の場合
            if num <= 0:
                print("1以上の数字を入力してください")
            # 1以上の数字が正常に入力された場合
            else:
                # numを返り値として終了
                return num

# 能力値決定関数
def decide_status():
    print('能力値を設定します。パンチ力・スピード・タフネスの3種類です。')
    print('1つの値の最大値は10で、3つの合計は15でなければいけません。')
    # パンチ力設定
    while True:
        punch_power = decide_num('パンチ力')
        # 最大値10をオーバーしている場合
        if punch_power > 10:
            print('最大値をオーバーしています。1つの能力値の最大値は10です。')
        else:
            # "数値種別:数値"を表示
            print("{}:{}".format('パンチ力',punch_power))
            break
    # スピード設定
    while True:
        speed = decide_num('スピード')
        # 最大値10をオーバーしている場合
        if speed > 10:
            print('最大値をオーバーしています。1つの能力値の最大値は10です。')
        # 2つの値の合計値が15を超えている場合
        elif (speed + punch_power) > 15:
            print('2つの値の合計値が{}です。3つの値の合計値は15で、オーバーしています。'.format(speed + punch_power))
        # パンチ力とスピードの合計が15の場合
        elif (speed + punch_power) == 15:
            print('パンチ力とスピードの合計値が{}です。3つの値の合計値は15で、その値ではタフネスに能力値を振れません。'.format(speed + punch_power))
        else:
            # "数値種別:数値"を表示
            print("{}:{}".format('スピード',speed))
            break
    # タフネス設定
    while True:
        toughness = decide_num('タフネス')
        # 最大値10をオーバーしている場合
        if toughness > 10:
            print('最大値をオーバーしています。1つの能力値の最大値は10です。')
        # 3つの値の合計値が15を超えている場合
        elif (speed + punch_power + toughness) > 15:
            print('3つの値の合計値が{}です。3つの値の合計値は15で、オーバーしています。'.format(speed + punch_power + toughness))
        elif (speed + punch_power + toughness) < 15:
            print('3つの値の合計値が{}です。3つの値の合計値は15で、{}足りません。'.format((speed + punch_power + toughness),15 - (speed + punch_power + toughness)))
        else:
            # "数値種別:数値"を表示
            print("{}:{}".format('タフネス',toughness))
            # 3つの値を返り値として終了
            return punch_power,speed,toughness

def knockout(log_title, log_text, current_round, offence_boxer, defense_boxer):
    print_text = 'レフェリーがカウントを数える。\n'
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = 'カウント１０！！\n'
    print(print_text)
    log_text += print_text + '\n'
    input()
    defense_boxer.result = '●'
    offence_boxer.result = '〇'
    print_text = 'カーン！カーン！カーン！　{}はKO負けした。\n\n'.format(defense_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = 'Winner {}！！\n'.format(offence_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    if offence_boxer.corner == '青':
        print_text = '{}{}（第{}R　KO）{}{}'.format(offence_boxer.result,offence_boxer.name,current_round,defense_boxer.name,defense_boxer.result)
        print(print_text)
        log_text += print_text + '\n'
    else:
        print_text = '{}{}（第{}R　KO）{}{}'.format(defense_boxer.result,defense_boxer.name,current_round,offence_boxer.name,offence_boxer.result)
        print(print_text)
        log_text += print_text + '\n'
    with open(log_title+'.txt', mode='w', encoding='utf-8') as f:
        f.write(log_text)
    input('キーを押したら終了します')
    return log_title, log_text, current_round, offence_boxer, defense_boxer

def technical_knockout(log_title, log_text, current_round, offence_boxer, defense_boxer):
    print_text = 'レフェリーが両腕を交差した。\n'
    print(print_text)
    log_text += print_text + '\n'
    defense_boxer.result = '●'
    offence_boxer.result = '〇'
    input()
    print_text = 'カーン！カーン！カーン！　{}はTKO負けした。\n\n'.format(defense_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = 'Winner {}！！\n'.format(offence_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    if offence_boxer.corner == '青':
        print_text = '{}{}（第{}R　TKO）{}{}'.format(offence_boxer.result,offence_boxer.name,current_round,defense_boxer.name,defense_boxer.result)
        print(print_text)
        log_text += print_text + '\n'
    else:
        print_text = '{}{}（第{}R　TKO）{}{}'.format(defense_boxer.result,defense_boxer.name,current_round,offence_boxer.name,offence_boxer.result)
        print(print_text)
        log_text += print_text + '\n'
    with open(log_title+'.txt', mode='w', encoding='utf-8') as f:
        f.write(log_text)
    input('キーを押したら終了します')
    return log_title, log_text, current_round, offence_boxer, defense_boxer

def standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type):
    if defense_boxer.speed <= 0:
        defense_boxer.speed = 1
        print_text = 'カウント8で立ち上がる。\n'
        print(print_text)
        log_text += print_text + '\n'
        input()
        print_text = '体力が{}に回復\n'.format(defense_boxer.hp)
        print(print_text)
        log_text += print_text + '\n'
        input()
        print_text = 'スピードが減って{}に。\n'.format(defense_boxer.speed)
        print(print_text)
        log_text += print_text + '\n'
        input()
        return log_title, log_text, current_round, offence_boxer, defense_boxer
    else:
        print_text = 'カウント8で立ち上がる。\n'
        print(print_text)
        log_text += print_text + '\n'
        input()
        print_text = '体力が{}に回復\n'.format(defense_boxer.hp)
        print(print_text)
        log_text += print_text + '\n'
        input()
        if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
            print_text = 'スピードが-4で{}に。\n'.format(defense_boxer.speed)
            print(print_text)
            log_text += print_text + '\n'
        else:
            print_text = 'スピードが-3で{}に。\n'.format(defense_boxer.speed)
            print(print_text)
            log_text += print_text + '\n'
        input()
        return log_title, log_text, current_round, offence_boxer, defense_boxer

def offence(log_title, log_text, current_round, offence_boxer, defense_boxer):
    offence_boxer.attack_num += 1
    print_text = '{}が攻撃の主導権を手にした。\n'.format(offence_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()

    offence_dice_6 = offence_boxer.dice_6.throw_dice()
    if offence_dice_6[0] == 1:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = 'ジャブ'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = 'ジャブの連打'
    elif offence_dice_6[0] == 2:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = '左ボディブロー'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = '右ボディブロー'
    elif offence_dice_6[0] == 3:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = '左ストレート'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = '右ストレート'
    elif offence_dice_6[0] == 4:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = '左フック'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = '右フック'
    elif offence_dice_6[0] == 5:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = '左アッパーカット'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = '右アッパーカット'
    elif offence_dice_6[0] == 6:
        if offence_dice_6[1] >= 1 and offence_dice_6[1] <= 3:
            offence_punch_type = 'カウンターパンチ'
        elif offence_dice_6[1] >= 4 and offence_dice_6[1] <= 6:
            offence_punch_type = '必殺技'
    if offence_punch_type == '必殺技' and offence_dice_6[1] >= 4 and offence_dice_6[1] <= 5:
        offence_attack_num = 12 + offence_boxer.punch_power - defense_boxer.toughness
    elif offence_punch_type == '必殺技' and offence_dice_6[1] == 6:
        offence_attack_num = 15 + offence_boxer.punch_power - defense_boxer.toughness
    else:
        offence_attack_num = sum(offence_dice_6) + offence_boxer.punch_power - defense_boxer.toughness
    print_text = '{}の攻撃！！ {}\n'.format(offence_boxer.name,offence_dice_6)
    print(print_text)
    log_text += print_text + '\n'

    if offence_attack_num < 1:
        input()
        defense_boxer.hp -= 1
        print_text = '{}のパンチが防御された。しかし、{}に1のダメージを与えた。'.format(offence_boxer.name,defense_boxer.name)
        print(print_text)
        log_text += print_text + '\n'
        input()
        if defense_boxer.hp <= 0:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 6:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) == 7:
                defense_boxer.hp = 1
                defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 8:
                defense_boxer.hp = 2
                defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        else:
            return log_title, log_text, current_round, offence_boxer, defense_boxer
    elif offence_punch_type == '必殺技':
        input()
        defense_boxer.hp -= offence_attack_num
        print_text = '{}の必殺技が炸裂した。{}-{}のダメージでHPが{}に減った。\n'.format(offence_boxer.name,defense_boxer.name,offence_attack_num,defense_boxer.hp)
        print(print_text)
        log_text += print_text + '\n'
        input()
        print_text = '{}がダウン！\n'.format(defense_boxer.name)
        print(print_text)
        log_text += print_text + '\n'
        input()
        if defense_boxer.hp >= 1:
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 5:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 6:
                print_text = 'カウント8で立ち上がる。\n'
                print(print_text)
                log_text += print_text + '\n'
                input()
                if defense_boxer.hp <= 39:
                    defense_boxer.hp += 1
                    print_text = '体力{}に回復。\n'.format(defense_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                    input()
                if defense_boxer.toughness <= 2:
                    defense_boxer.toughness = 1
                    print_text = 'タフネスが{}に。\n'.format(defense_boxer.toughness)
                    print(print_text)
                    log_text += print_text + '\n'
                else:
                    defense_boxer.toughness -= 2
                    print_text = 'タフネスが-2で{}に。\n'.format(defense_boxer.toughness)
                    print(print_text)
                    log_text += print_text + '\n'
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp >= -3 and defense_boxer.hp <= 0:
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 6:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 7:
                print_text = 'カウント8で立ち上がる。\n'
                print(print_text)
                log_text += print_text + '\n'
                input()
                defense_boxer.hp = 1
                print_text = '体力が{}に回復。\n'.format(defense_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                input()
                if defense_boxer.toughness <= 2:
                    defense_boxer.toughness = 1
                    print_text = 'タフネスが{}に。\n'.format(defense_boxer.toughness)
                    print(print_text)
                    log_text += print_text + '\n'
                else:
                    defense_boxer.toughness -= 2
                    print_text = 'タフネスが-2で{}に。\n'.format(defense_boxer.toughness)
                    print(print_text)
                    log_text += print_text + '\n'
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp <= -4:
            log_title, log_text, current_round, offence_boxer, defense_boxer = technical_knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
            return log_title, log_text, current_round, offence_boxer, defense_boxer
    else:
        input()
        defense_boxer.hp -= offence_attack_num
        print_text = '{}の{}がヒットした。{}-{}のダメージでHPが{}に減った。\n'.format(offence_boxer.name,offence_punch_type,defense_boxer.name,offence_attack_num,defense_boxer.hp)
        print(print_text)
        log_text += print_text + '\n'
        input()
        if 40 >= defense_boxer.hp >= 20 and offence_attack_num >= 13:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 3:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 4 and sum(defense_dice_6) <= 7:
                if defense_boxer.hp <= 39:
                    defense_boxer.hp += 1
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer          
            elif sum(defense_dice_6) >= 8:
                if defense_boxer.hp <= 38:
                    defense_boxer.hp += 2
                elif defense_boxer.hp == 39:
                    defense_boxer.hp += 1
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp >= 11 and defense_boxer.hp <= 19 and offence_attack_num >= 12:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 4:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 5 and sum(defense_dice_6) <= 7:
                defense_boxer.hp += 1
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 8:
                defense_boxer.hp += 2
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp >= 1 and defense_boxer.hp <= 9 and offence_attack_num >= 7:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 5:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 6 and sum(defense_dice_6) <= 7:
                defense_boxer.hp += 1
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) >= 8:
                defense_boxer.hp += 2
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp >= -3 and defense_boxer.hp <= 0:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            defense_dice_6 = defense_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(defense_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            input()
            if sum(defense_dice_6) <= 6:
                log_title, log_text, current_round, offence_boxer, defense_boxer = knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
            elif sum(defense_dice_6) == 7:
                defense_boxer.hp = 1
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer           
            elif sum(defense_dice_6) >= 8:
                defense_boxer.hp = 2
                if offence_punch_type == '左フック' or offence_punch_type == '右フック' or offence_punch_type == '左アッパーカット' or offence_punch_type == '右アッパーカット' or offence_punch_type == 'カウンターパンチ':
                    defense_boxer.speed -= 4
                else:
                    defense_boxer.speed -= 3
                log_title, log_text, current_round, offence_boxer, defense_boxer = standup_a(log_title, log_text, current_round, offence_boxer, defense_boxer, offence_punch_type)
                return log_title, log_text, current_round, offence_boxer, defense_boxer
        elif defense_boxer.hp <= -4:
            print_text = '{}がダウン！\n'.format(defense_boxer.name)
            print(print_text)
            log_text += print_text + '\n'
            input()
            log_title, log_text, current_round, offence_boxer, defense_boxer = technical_knockout(log_title, log_text, current_round, offence_boxer, defense_boxer)
            return log_title, log_text, current_round, offence_boxer, defense_boxer
        else:
            return log_title, log_text, current_round, offence_boxer, defense_boxer

def match(FIGHT_LOG_DIR,max_round,red_boxer,blue_boxer):
    fight_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    match_title = '{}_{}_VS_{}'.format(fight_datetime, blue_boxer.name, red_boxer.name)
    log_title = FIGHT_LOG_DIR + '/' + match_title
    log_text = ''
    log_text += match_title + '\n'
    print_text = ''
    max_round = max_round
    current_round = 1
    current_turn = 1
    print_text = 'メインイベント女子ボクシング{}回戦を行います！！\n'.format(max_round)
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = '{}コーナー{}！！\n'.format(blue_boxer.corner, blue_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = '{}コーナー{}！！\n'.format(red_boxer.corner, red_boxer.name)
    print(print_text)
    log_text += print_text + '\n'
    input()
    print_text = '試合開始！\n'
    print(print_text)
    log_text += print_text + '\n'
    while current_round <= max_round and red_boxer.result == '' and blue_boxer.result == '':
        input()
        red_dice_12 = red_boxer.dice_12.throw_dice()
        blue_dice_12 = blue_boxer.dice_12.throw_dice()
        red_dice_12_sum = sum(red_dice_12) + red_boxer.speed
        blue_dice_12_sum = sum(blue_dice_12) + blue_boxer.speed

        print_text = '第{}R ターン{}\n'.format(current_round,current_turn)
        print(print_text)
        log_text += print_text + '\n'
        input()

        print_text = '{}のダイス数値が{}に対し{}のダイス数値が{}\n'.format(red_boxer.name, red_dice_12_sum,blue_boxer.name,blue_dice_12_sum)
        print(print_text)
        log_text += print_text + '\n'
        input()
        
        if red_dice_12_sum > blue_dice_12_sum:
            log_title, log_text, current_round, red_boxer, blue_boxer = offence(log_title, log_text, current_round, red_boxer, blue_boxer)
            if red_boxer.result == '〇' and blue_boxer.result == '●':
                break

        elif blue_dice_12_sum > red_dice_12_sum:
            log_title, log_text, current_round, blue_boxer, red_boxer = offence(log_title, log_text, current_round, blue_boxer, red_boxer)
            if blue_boxer.result == '〇' and red_boxer.result == '●':
                break

        else:
            print_text = '両者クリンチ。\n'
            print(print_text)
            log_text += print_text + '\n'
            input()
            if red_boxer.hp <= 38:
                red_boxer.hp += 2
                print_text = '{}、体力が2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                input()
            elif red_boxer.hp == 39:
                red_boxer.hp += 1
                print_text = '{}、体力が1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                input()
            if blue_boxer.hp <= 38:
                blue_boxer.hp += 2
                print_text = '{}、体力が2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                input()
            elif blue_boxer.hp == 39:
                blue_boxer.hp += 1
                print_text = '{}、体力が1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                input()
                    
        if current_turn == 3:
            input()
            print_text = 'カーン！\n第{}R終了のゴングが鳴った。\n'.format(current_round)
            print(print_text)
            log_text += print_text + '\n'
            current_turn = 1
            current_round += 1
            input()

            if current_round > max_round:
                print_text = 'カーン！カーン！カーン！　試合終了のゴングが鳴った。\n'
                print(print_text)
                log_text += print_text + '\n'
                input()
                print_text = '判定の結果をお伝えします！\n'
                print(print_text)
                log_text += print_text + '\n'
                input()
                print_text = '赤コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(red_boxer.name,red_boxer.hp,red_boxer.punch_power,red_boxer.speed,red_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
                input()
                print_text = '青コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.punch_power,blue_boxer.speed,blue_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
                input()

                if blue_boxer.hp > red_boxer.hp:
                    print_text = 'Winner {}！！\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    input()
                    print_text = '〇{}（{}R　判定）{}●'.format(blue_boxer.name,max_round,red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title+'.txt', mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
                elif red_boxer.hp > blue_boxer.hp:
                    print_text = 'Winner {}！！\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    input()
                    print_text = '●{}（{}R　判定）{}〇'.format(blue_boxer.name,max_round,red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title+'.txt', mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
                else:
                    print_text = 'Draw！！\n'
                    print(print_text)
                    log_text += print_text + '\n'
                    input()
                    print_text = '{}（{}R　判定引き分け）{}'.format(blue_boxer.name,max_round,red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title+'.txt', mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
            else:
                print_text = 'インターバル\n'
                print(print_text)
                log_text += print_text + '\n'
                input()
                # 青コーナーのボクサーが体力38以下の場合
                if blue_boxer.hp <= 38:
                    # インターバルで体力2加算
                    blue_boxer.hp += 2
                    # ラウンド中の攻撃回数が赤より多かった場合
                    if blue_boxer.attack_num > red_boxer.attack_num:
                        # スピードが1以下だったら減算せず
                        if blue_boxer.speed <= 1:
                            print_text = '青コーナー：{}の体力が2回復して{}になった。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                        # スピードが2以上の場合攻め疲れで-1
                        else:
                            blue_boxer.speed -= 1
                            print_text = '青コーナー：{}の体力が2回復して{}になった。攻め疲れでスピード-1で{}に。\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                    # 赤より攻撃回数が少ない場合体力の2加算のみ
                    else:
                        print_text = '青コーナー：{}の体力が2回復して{}になった。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        input()
                elif blue_boxer.hp == 39:
                    blue_boxer.hp += 1
                    if blue_boxer.attack_num > red_boxer.attack_num:
                        if blue_boxer.speed <= 1:
                            print_text = '青コーナー：{}の体力が1回復して{}になった。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                        else:
                            blue_boxer.speed -= 1
                            print_text = '青コーナー：{}の体力が1回復して{}になった。攻め疲れでスピード-1で{}に。\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                    else:
                        print_text = '青コーナー：{}の体力が1回復して{}になった。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        input()
                else:
                    if blue_boxer.attack_num > red_boxer.attack_num:
                        if blue_boxer.speed <= 1:
                            input()
                        else:
                            blue_boxer.speed -= 1
                            print_text = '青コーナー：{}攻め疲れでスピード-1で{}に。\n'.format(blue_boxer.name,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                if red_boxer.hp <= 38:
                    red_boxer.hp += 2
                    if red_boxer.attack_num > blue_boxer.attack_num:
                        if red_boxer.speed <= 1:
                            print_text = '赤コーナー：{}の体力が2回復して{}になった。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                        else:
                            red_boxer.speed -= 1
                            print_text = '赤コーナー：{}の体力が2回復して{}になった。攻め疲れでスピード-1で{}に。\n'.format(red_boxer.name,red_boxer.hp,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                    else:
                        print_text = '赤コーナー：{}の体力が2回復して{}になった。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        input()
                elif red_boxer.hp == 39:
                    red_boxer.hp += 1
                    if red_boxer.attack_num > blue_boxer.attack_num:
                        if red_boxer.speed <= 1:
                            print_text = '赤コーナー：{}の体力が1回復して{}になった。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                        else:
                            red_boxer.speed -= 1
                            print_text = '赤コーナー：{}の体力が2回復して{}になった。攻め疲れでスピード-1で{}に。\n'.format(red_boxer.name,red_boxer.hp,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                    else:
                        print_text = '赤コーナー：{}の体力が1回復して{}になった。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        input()
                else:
                    if red_boxer.attack_num > blue_boxer.attack_num:
                        if red_boxer.speed <= 1:
                            input()
                        else:
                            red_boxer.speed -= 1
                            print_text = '赤コーナー：{}攻め疲れでスピード-1で{}に。\n'.format(red_boxer.name,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                            input()
                red_boxer.attack_num = 0
                blue_boxer.attack_num = 0
                print_text = '青コーナー：{}選手\nHP:{}\nパンチ力：{}\nスピード：{}\nタフネス：{}\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.punch_power,blue_boxer.speed,blue_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
                input()
                print_text = '赤コーナー：{}選手\nHP：{}\nパンチ力：{}\nスピード：{}\nタフネス：{}\n'.format(red_boxer.name,red_boxer.hp,red_boxer.punch_power,red_boxer.speed,red_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
        else:
            current_turn += 1

# 対戦ログ保存フォルダ作成
FIGHT_LOG_DIR = make_folder()

# 12面ダイス2個を作成
dice_12 = Dice(2,12)
# 6面ダイス2個を作成
dice_6 = Dice(2,6)

# 青コーナーのボクサー作成プロセス
print('青コーナーのボクサーを作成します')
# 名前設定
name = input('名前を入力してください:')
# 能力値設定
punch_power,speed,toughness = decide_status()
# ボクサー作成
print('')
blue_boxer = Boxer('青', name, punch_power,speed,toughness, dice_12, dice_6)
print('')

# 赤コーナーのボクサー作成プロセス
print('赤コーナーのボクサーを作成します')
# 名前設定
name = input('名前を入力してください:')
# 能力値設定
punch_power,speed,toughness = decide_status()
# ボクサー作成
print('')
red_boxer = Boxer('赤', name, punch_power,speed,toughness, dice_12, dice_6)
print('')

# 最大ラウンド数
max_round = decide_num('試合の最大ラウンド数')

match(FIGHT_LOG_DIR,max_round,red_boxer,blue_boxer)