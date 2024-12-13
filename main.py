from Infrastructure.database import SessionLocal
from Infrastructure.DatabaseUserRepository import DatabaseUserRepository
from Controllers.UserController import UserController
from UseCases.CreateUser import CreateUserUseCase

# Tạo session
db = SessionLocal()

# Tạo repository sử dụng Database
user_repository = DatabaseUserRepository(db)

# Tạo use case
create_user_use_case = CreateUserUseCase(user_repository)

# Tạo controller
user_controller = UserController(create_user_use_case)

# Tạo người dùng mới
user_controller.create_user("tigersky.ntp@gmail.com", "password123")  # Expected: "User created successfully."
#user_controller.create_user("test@example.com", "password456")  # Expected: "User with this email already exists."

# Đóng session
db.close()