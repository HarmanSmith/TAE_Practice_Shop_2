class StandardUser:

    user_standard = "standard_user"
    user_locked_out = "locked_out_user"
    user_problem = "problem_user"
    user_performance = "performance_glitch_user"
    password = "secret_sauce"

    def get_username_standard(self):
        return self.user_standard

    def get_username_locked(self):
        return self.user_locked_out

    def get_username_problem(self):
        return self.user_problem

    def get_username_performance(self):
        return self.user_performance

    def get_password(self):
        return self.password
