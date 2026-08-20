import blouch2

result = blouch2.check_key()
if result:
    user_name, user_key, expiry_str = result
    remaining_time = blouch2.calculate_time_left(expiry_str)
    blouch2.display_welcome_banner(user_name, user_key, remaining_time)
    blouch2.hold_screen_10_seconds()
    blouch2.BNG_71_()
