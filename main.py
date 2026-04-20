from src.quiz import Quiz
from src.game import QuizGame

# 기본 퀴즈 데이터셋
quiz_list = [
    Quiz("나의 전공은?", ["1. 철학", "2. 컴퓨터공학", "3. 정치외교학", "4. 영어영문학"], 1),
    Quiz("코디세이 참여 이유?", ["1. 친구 권유", "2. 프로그래밍 흥미", "3. 장학금", "4. 새 자극"], 2),
    Quiz("개발 프로그램 참여 경험?(코디세이 제외)", ["1. 0회", "2. 1회", "3. 2회", "4. 3회 이상"], 1),
    Quiz("현재 관심 분야는?", ["1. 빅 데이터", "2. AI", "3. IoT", "4. 앱 개발"], 2),
    Quiz("나의 MBTI는?", ["1. INTJ", "2. INFJ", "3. INFP", "4. INTP"], 3),
]      
if __name__ == "__main__":
    game = QuizGame(quiz_list) 
    game.load_data()

    try: 
        while True: 
            user_choice = game.display_menu()

            if user_choice == "1":
                game.run_quiz()

            elif user_choice == "2":
                game.add_quiz()
                game.save_data()
        
            elif user_choice == "3":
                game.show_quiz_list()

            elif user_choice == "4":
                print(f"\n현재 최고 점수는 {game.best_score}점입니다.")

            elif user_choice == "5":
                game.save_data()
                print("퀴즈 풀기를 종료합니다.")
                break 
            
            else:
                print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

    except KeyboardInterrupt:
        print("\n사용자에 의해 강제 종료 신호(Ctrl+C)가 감지되었습니다.")
        game.save_data() 
        print("데이터를 안전하게 저장한 후 프로그램을 종료합니다.")

    except EOFError as e: 
        print(f"\n예상치 못한 오류가 발생했습니다: {e}")
        game.save_data()