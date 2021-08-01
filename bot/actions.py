from .models import chats


def bot_responses(input_msg, name):
    user_msg = str(input_msg).lower()

    if user_msg == "stupid":
        joke = """Yo' Mama is so stupid, she needs a recipe to make ice cubes."""
        if chats.objects.filter(Username=name).exists():
            user = chats.objects.get(Username=name)
            user.button_stupid += 1
            user.save()
            return joke, user
        else:
            user = chats.objects.create(Username=name, button_stupid=1)
            return joke, user

    elif user_msg == "fat":
        joke = """Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate."""
        if chats.objects.filter(Username=name).exists():
            user = chats.objects.get(Username=name)
            user.button_fat += 1
            user.save()
            return joke, user
        else:
            user = chats.objects.create(Username=name, button_fat=1)
            return joke, user
    elif user_msg == "dumb":
        joke = """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick."""
        if chats.objects.filter(Username=name).exists():
            user = chats.objects.get(Username=name)
            user.button_dumb += 1
            user.save()
            return joke, user
        else:
            user = chats.objects.create(Username=name, button_dumb=1)
            return joke, user
    else:
        joke = "Sorry! Im still learning."
        user = name
        return joke, user