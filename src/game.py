import json
from src.quiz import Quiz

# 퀴즈 게임 클래스
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
        
        except (FileNotFoundError, json.JSONDecodeError, KeyError): 
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
                print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
            

    def run_quiz(self): # 세 번째 메서드
        print("\n퀴즈 게임을 시작합니다.")
        self.score = 0 

        for quiz in self.quizzes: 
            print(f"\n질문: {quiz.question}")
            for option in quiz.options:
                print(option)

            # 1. 공백 입력을 방지하고 값을 받을 때까지 반복
            while True:
                answer = input("정답 번호 입력: ").strip()
                
                # 입력값이 비어있는 경우 (공백 처리)
                if not answer:
                    print("⚠️ 정답 번호를 입력해야 합니다.")
                    continue
                
                # 숫자가 아닌 문자나 특수기호가 포함된 경우
                if not answer.isdigit():
                    print("⚠️ 문자가 아닌 '숫자'로만 입력해주세요.")
                    continue
                
                if 1 <= int(answer) <= 4:
                    break 
                else:
                    print("⚠️ 보기에 있는 번호(1~4)를 입력해주세요.")
                    continue

                # 모든 조건을 통과하면 루프 탈출
                break
            
            # 2. 정답 체크 (while 루프 밖, for 루프 안)
            if answer == str(quiz.answer):
                print("정답입니다!")
                self.score += 1 
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")
        
        # 3. 모든 문제를 다 푼 후 결과 출력 (for 루프 밖)
        print(f"\n모든 문제를 풀었습니다. 최종 점수: {self.score} / {len(self.quizzes)}")

        if self.score > self.best_score:
            print(f"축하합니다. 최고 점수가 갱신되었습니다! ({self.best_score} -> {self.score})")
            self.best_score = self.score
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")


    def add_quiz(self): # 네 번째 메서드
        print("\n새로운 퀴즈 추가 (취소하려면 'q'를 입력하세요)")
        
        # 1. 질문 입력 시 공백 체크 루프
        while True:
            question = input("질문을 입력하세요: ").strip()
            
            if not question: # 공백 입력 시
                print("⚠️ 질문 내용을 입력해야 합니다.")
                continue
            
            if question.lower() == 'q': # 취소 로직
                print("취소되었습니다.")
                return
            
            break # 정상 입력 시 루프 탈출

        # 2. 보기 입력 (여기에도 공백 체크를 넣으면 더 좋습니다)
        options = []
        for i in range(1, 5):
            while True:
                opt = input(f"{i}번 보기를 입력하세요: ").strip()
                if opt:
                    options.append(f"{i}. {opt}")
                    break
                print(f"⚠️ {i}번 보기 내용을 입력해주세요.")

        # 3. 정답 번호 입력 (기존 코드 유지)
        while True:
            try: 
                answer = input("정답 번호를 입력하세요: ").strip()
                if not answer:
                    print("⚠️ 정답 번호를 입력하세요.")
                    continue
                
                answer = int(answer)

                if 1 <= answer <= 4:
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
