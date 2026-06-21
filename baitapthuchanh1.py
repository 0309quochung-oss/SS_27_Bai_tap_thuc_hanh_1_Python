class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def theory_score(self):
        return self.__theory_score

    @property
    def practice_score(self):
        return self.__practice_score

    @property
    def project_score(self):
        return self.__project_score

    @property
    def final_score(self):
        return self.__final_score

    @property
    def academic_rank(self):
        return self.__academic_rank

    def update_theory_score(self, score):
        self.__theory_score = score

    def update_practice_score(self, score):
        self.__practice_score = score

    def update_project_score(self, score):
        self.__project_score = score

    def calculate_final_score(self):
        self.__final_score = (
            self.__theory_score * 0.2
            + self.__practice_score * 0.3
            + self.__project_score * 0.5
        )

    def classify_academic_rank(self):
        if self.__final_score >= 8.5:
            self.__academic_rank = "Giỏi"
        elif self.__final_score >= 7:
            self.__academic_rank = "Khá"
        elif self.__final_score >= 5:
            self.__academic_rank = "Trung bình"
        else:
            self.__academic_rank = "Yếu"


class StudentManager:
    def __init__(self):
        self.students = []

    def find_id(self, id):
        for stu in self.students:
            if stu.id == id:
                return stu
        return None

    def add_student(self):
        stu_id = input("Nhập mã SV: ").strip()

        if not stu_id:
            print("Mã SV không được để trống")
            return

        if self.find_id(stu_id):
            print("Mã SV đã tồn tại")
            return

        stu_name = input("Nhập họ tên: ").strip()

        if not stu_name:
            print("Tên không được để trống")
            return

        try:
            theory = float(input("Nhập điểm lý thuyết: "))
            practice = float(input("Nhập điểm thực hành: "))
            project = float(input("Nhập điểm đồ án: "))
        except ValueError:
            print("Điểm phải là số")
            return

        if not (0 <= theory <= 10):
            print("Điểm lý thuyết không hợp lệ")
            return

        if not (0 <= practice <= 10):
            print("Điểm thực hành không hợp lệ")
            return

        if not (0 <= project <= 10):
            print("Điểm đồ án không hợp lệ")
            return

        student = Student(
            stu_id,
            stu_name,
            theory,
            practice,
            project
        )

        student.calculate_final_score()
        student.classify_academic_rank()

        self.students.append(student)

        print("Thêm sinh viên thành công")

    def show_all(self):
        if not self.students:
            print("Danh sách trống")
            return

        print("-" * 120)

        print(
            f"{'Mã SV':<10}"
            f"{'Họ tên':<25}"
            f"{'LT':<10}"
            f"{'TH':<10}"
            f"{'DA':<10}"
            f"{'TK':<10}"
            f"{'Học lực':<15}"
        )

        print("-" * 120)

        for stu in self.students:
            print(
                f"{stu.id:<10}"
                f"{stu.name:<25}"
                f"{stu.theory_score:<10}"
                f"{stu.practice_score:<10}"
                f"{stu.project_score:<10}"
                f"{stu.final_score:<10.2f}"
                f"{stu.academic_rank:<15}"
            )

    def update_student(self):
        stu_id = input("Nhập mã SV cần cập nhật: ")

        student = self.find_id(stu_id)

        if not student:
            print("Không tìm thấy sinh viên")
            return

        try:
            theory = float(input("Nhập điểm lý thuyết mới: "))
            practice = float(input("Nhập điểm thực hành mới: "))
            project = float(input("Nhập điểm đồ án mới: "))
        except ValueError:
            print("Điểm phải là số")
            return

        if not (0 <= theory <= 10):
            print("Điểm không hợp lệ")
            return

        if not (0 <= practice <= 10):
            print("Điểm không hợp lệ")
            return

        if not (0 <= project <= 10):
            print("Điểm không hợp lệ")
            return

        student.update_theory_score(theory)
        student.update_practice_score(practice)
        student.update_project_score(project)

        student.calculate_final_score()
        student.classify_academic_rank()

        print("Cập nhật thành công")

    def delete_student(self):
        stu_id = input("Nhập mã SV cần xóa: ")

        student = self.find_id(stu_id)

        if not student:
            print("Không tìm thấy sinh viên")
            return

        confirm = input(
            "Bạn có chắc muốn xóa sinh viên này không? (Y/N): "
        )

        if confirm.lower() == "y":
            self.students.remove(student)
            print("Xóa thành công")
        else:
            print("Đã hủy thao tác")

    def search_student(self):
        keyword = input("Nhập tên cần tìm: ").lower()

        result = []

        for stu in self.students:
            if keyword in stu.name.lower():
                result.append(stu)

        if not result:
            print("Không tìm thấy sinh viên phù hợp")
            return

        print("-" * 120)

        for stu in result:
            print(
                f"{stu.id} | "
                f"{stu.name} | "
                f"{stu.final_score:.2f} | "
                f"{stu.academic_rank}"
            )


def main():
    manager = StudentManager()

    while True:
        print("\n========== MENU ==========")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Thoát")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            manager.add_student()

        elif choice == "3":
            manager.update_student()

        elif choice == "4":
            manager.delete_student()

        elif choice == "5":
            manager.search_student()

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!")
            break

        else:
            print("Lựa chọn không hợp lệ")


main()