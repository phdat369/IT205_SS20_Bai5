import logging
players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]
logging.basicConfig(
    filename="fantasy_league.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def display_market(player_list):
    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    if len(player_list) == 0:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return
    print(
        f"{'ID':<10} | "
        f"{'Tên tuyển thủ':<15} | "
        f"{'Giá trị':<10} | "
        f"{'Fan Token':<10} | "
        f"{'Điểm':<10} | "
        f"{'Hệ số':<8} | "
        f"{'Trạng thái đầu tư'}"
    )
    print("-" * 110)
    for player in player_list:
        fan_tokens = player.get("fan_tokens", 0)
        if fan_tokens == 0:
            investment_status = "Chưa có người đầu tư"
        elif fan_tokens <= 1000:
            investment_status = "Đang thu hút"
        else:
            investment_status = "Tuyển thủ Hot"
        print(
            f"{player.get('player_id', 'Unknown'):<10} | "
            f"{player.get('name', 'Unknown'):<15} | "
            f"{player.get('market_value', 0):<10} | "
            f"{fan_tokens:<10} | "
            f"{player.get('match_points', 0):<10} | "
            f"{player.get('form_multiplier', 1.0):<8} | "
            f"{investment_status}"
        )
    logging.info("User viewed the player market.")
def invest_tokens(player_list):
    print("\n--- ĐẦU TƯ FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    found = False
    for player in player_list:
        if player["player_id"] == player_id:
            found = True
            while True:
                try:
                    token = int(
                        input("Nhập số token muốn đầu tư: "))
                    if token <= 0:
                        print(
                            "Số token phải là số nguyên dương. "
                            "Vui lòng nhập lại."
                        )
                        continue
                    break
                except ValueError:
                    print(
                        "Số token phải là số nguyên dương. "
                        "Vui lòng nhập lại."
                    )
                    logging.warning("Invalid token input while investing")
            player["fan_tokens"] += token
            print(
                f"\nThành công: Đã đầu tư {token} token "
                f"vào tuyển thủ {player_id}."
            )
            print(
                f"Số Fan Token hiện tại của "
                f"{player['name']}: {player['fan_tokens']:,}"
            )
            logging.info(f"Invested {token} tokens into {player_id}")
            break
    if found is False:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(f"Invest failed - Player {player_id} not found")
def withdraw_tokens(player_list):
    print("\n--- RÚT VỐN FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    found = False
    for player in player_list:
        if player["player_id"] == player_id:
            found = True
            while True:
                try:
                    token = int(
                        input("Nhập số token muốn rút: "))
                    if token <= 0:
                        print("Số token phải là số nguyên dương.")
                        continue
                    break
                except ValueError:
                    print("Số token phải là số nguyên dương.")
            if token > player["fan_tokens"]:
                print(
                    "Không thể rút. Số token muốn rút vượt quá "
                    "số Fan Token hiện có."
                )
                print(
                    f"Fan Token hiện có của "
                    f"{player['name']}: {player['fan_tokens']}"
                )
                logging.warning("Withdraw failed - Amount exceeds current fan tokens")
                break
            fee = token * 0.1
            actual_received = token - fee
            player["fan_tokens"] -= token
            print(
                f"\nThành công: Đã rút {token} token "
                f"khỏi tuyển thủ {player_id}."
            )
            print(f"Phí giao dịch 10%: {fee} token")
            print(
                f"Số token thực nhận về ví: "
                f"{actual_received} token"
            )
            print(
                f"Fan Token còn lại của "
                f"{player['name']}: {player['fan_tokens']:,}"
            )
            logging.info(
                f"Withdrawn {token} tokens from "
                f"{player_id}. Actual received: "
                f"{actual_received}"
            )
            break
    if found is False:
        print("Không tìm thấy tuyển thủ!")
def update_form(player_list):
    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    found = False
    for player in player_list:
        if player["player_id"] == player_id:
            found = True
            while True:
                try:
                    multiplier = float(
                        input(
                            "Nhập hệ số phong độ mới "
                            "(0.5 - 2.5): "
                        )
                    )
                    if multiplier < 0.5 or multiplier > 2.5:
                        print(
                            "Hệ số phong độ chỉ được nằm "
                            "trong khoảng 0.5 đến 2.5."
                        )
                        continue
                    break
                except ValueError:
                    print(
                        "Hệ số phong độ phải là số thực. "
                        "Vui lòng nhập lại."
                    )
            player["form_multiplier"] = multiplier
            print(
                f"\nThành công: Đã cập nhật hệ số "
                f"phong độ cho {player['name']}."
            )
            print(f"Hệ số mới: x{multiplier}")
            logging.info(
                f"Updated form multiplier for "
                f"{player_id} to {multiplier}"
            )
            break
    if found is False:
        print("Không tìm thấy tuyển thủ!")
def calculate_match_points(player_list):
    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    found = False
    for player in player_list:
        if player["player_id"] == player_id:
            found = True
            while True:
                try:
                    base_points = float(
                        input("Nhập điểm gốc của trận đấu: "))
                    if base_points < 0:
                        print("Điểm không được âm.")
                        continue
                    break
                except ValueError:
                    print(
                        "Điểm phải là số."
                    )
            earned_points = (
                base_points *
                player["form_multiplier"]
            )
            player["match_points"] += earned_points
            print(
                f"\n>> Tuyển thủ {player['name']} "
                f"nhận được {earned_points} điểm "
                f"(Hệ số x{player['form_multiplier']})."
            )
            print(
                f"Tổng điểm: "
                f"{player['match_points']}"
            )
            logging.info(
                f"Added {earned_points} "
                f"match points to {player_id}"
            )
            break
    if found is False:
        print("Không tìm thấy tuyển thủ!")
def main():
    while True:
        choose = input("""
===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====
1. Xem Sàn Giao Dịch Tuyển Thủ
2. Đầu tư Fan Token
3. Rút vốn (Hoàn trả Token)
4. Biến động phong độ (Cập nhật hệ số)
5. Chấm điểm sau trận đấu
6. Thoát hệ thống
==================================================
Chọn chức năng (1-6): """)
        if choose == "1":
            display_market(players)
        elif choose == "2":
            invest_tokens(players)
        elif choose == "3":
            withdraw_tokens(players)
        elif choose == "4":
            update_form(players)
        elif choose == "5":
            calculate_match_points(players)
        elif choose == "6":
            logging.info("Fantasy league system closed.")
            print("Đóng hệ thống Rikkei Esports Fantasy.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            logging.warning("Invalid menu choice selected")
main()