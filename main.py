import json

# (1) 퀴즈 클래스
class Quiz:
    def __init__(self, question, choices, answer): # 첫 번째 메서드
        self.question = question  
        self.options = choices    
        self.answer = answer

quiz_list = [
    Quiz("나의 전공은?", ["1. 철학", "2. 컴퓨터공학", "3. 정치외교학", "4. 영어영문학"], 1),
    Quiz("코디세이 참여 이유?", ["1. 친구 권유", "2. 프로그래밍 흥미", "3. 장학금", "4. 새 자극"], 2),
    Quiz("개발 프로그램 참여 경험?(코디세이 제외)", ["1. 0회", "2. 1회", "3. 2회", "4. 3회 이상"], 1),
    Quiz("현재 관심 분야는?", ["1. 빅 데이터", "2. AI", "3. IoT", "4. 앱 개발"], 2),
    Quiz("나의 MBTI는?", ["1. INTJ", "2. INFJ", "3. INFP", "4. INTP"], 3),
]      


# (2) 퀴즈 게임 클래스
class QuizGame:
    def __init__(self, quizzes): # 첫 번째 메서드
        self.quizzes = quizzes
        self.score = 0
        self.best_score = 0
        
    def save_data(self): # 여섯 번째 메서드 
        quiz_data_list = []
        for quiz in self.quizzes:
            quiz_data_list.append({
                "question": quiz.question,
                "options": quiz.options,
                "answer": quiz.answer
            })
            
        all_data = {
            "quizzes": quiz_data_list,
            "best_score": self.best_score
        }

        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)
        
        print("\n모든 데이터가 파일에 저장되었습니다.")


    def load_data(self): # 일곱 번째 메서드
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                all_data = json.load(f)
                
                self.best_score = all_data.get("best_score", 0)

                self.quizzes = []
                for item in all_data["quizzes"]: 
                    self.quizzes.append(Quiz(item["question"], item["options"], item["answer"]))
                
                print(f"\n기존 데이터를 성공적으로 불러왔습니다. (현재 최고 점수: {self.best_score}점)")
        
        except (FileNotFoundError, json.JSONDecodeError): 
            print("\n저장된 파일이 없습니다. 기존 퀴즈로 시작합니다.")
            self.best_score = 0


    def display_menu(self): # 두 번째 메서드
        while True: 
            print("\n=== 퀴즈 게임 메뉴 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = input("선택: ").strip()

            if not choice:
                print("⚠️ 메뉴 번호를 입력해주세요.")
                continue

            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("⚠️ 1~5 사이의 숫자를 입력해주세요.")
            

    def run_quiz(self): # 세 번째 메서드
            print("\n퀴즈 게임을 시작합니다.")
            self.score = 0 

            for quiz in self.quizzes: 
                print(f"\n질문: {quiz.question}")
                for option in quiz.options:
                    print(option)

                answer = input("정답 번호 입력: ")

                if answer == str(quiz.answer):
                    print("정답입니다!")
                    self.score += 1 
                else:
                    print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")
                
            print(f"모든 문제를 풀었습니다. 최종 점수: {self.score} / {len(self.quizzes)}")

            if self.score > self.best_score:
                print(f"축하합니다. 최고 점수가 갱신되었습니다! ({self.best_score} -> {self.score})")
                self.best_score = self.score
            else:
                print(f"현재 최고 점수는 {self.best_score}점입니다.")


    def add_quiz(self): # 네 번째 메서드
        print("\n새로운 퀴즈 추가 (취소하려면 'q'를 입력하세요)")
        question = input("질문을 입력하세요: ").strip()

        if question.lower() == 'q':
            print("취소되었습니다.")
            return

        options = []
        for i in range(1, 5):
            opt = input(f"{i}번 보기를 입력하세요: ").strip()
            options.append(f"{i}. {opt}")

        while True:
            try: 
                answer = input("정답 번호를 입력하세요: ").strip()
                if not answer:
                    print("정답 번호를 입력하세요.")
                    continue
                
                answer = int(answer_input)

                if 1 <= answer <=4:
                    break 
                else:
                    print("⚠️ 1에서 4 사이의 숫자만 입력 가능합니다.")
            except ValueError:
                print("⚠️ 문자가 아닌 '숫자'를 입력해주세요.")

        new_quiz = Quiz(question, options, answer)

        self.quizzes.append(new_quiz)
        print("퀴즈가 성공적으로 추가되었습니다!")


    def show_quiz_list(self): # 다섯 번째 메서드
        print("\n현재 퀴즈 목록")
        if not self. quizzes: 
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, 1): 
            print(f"{i}. {quiz.question}")

    def show_score(self):
        print(f"\n현재 당신의 점수는 {self.score}점입니다.")
        print(f"현재 최고 점수는 {self.best_score}점입니다.")

        if self.score == len(self.quizzes):
            print("축하해요! 모든 문제를 맞혔습니다!")
        
        elif self.score >= 4:
            print("대단해요! 거의 다 맞혔네요.")

        elif self.score > 0:
            print("아쉬워요! 한 번 더 도전해보세요.")

        else:
            print("아직은 0점이네요. 1번을 눌러 퀴즈를 풀어보세요.")


# (3) 실행 부분
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