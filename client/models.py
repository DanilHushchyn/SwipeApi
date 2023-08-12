from django.db import models

from builder.models import *


class AdvertDocument(models.TextChoices):
    OWN = "Собственность", "Собственность"
    INHERITANCE = (
        "Свидетельство о праве на наследство",
        "Свидетельство о праве на наследство",
    )


class AdvertAppointment(models.TextChoices):
    APARTMENTS = "Дом", "Дом"
    FLAT = "Квартира", "Квартира"
    COMMERCIAL = "Коммерческие помещения", "Коммерческие помещения"
    OFFICE = "Офисное помещение", "Офисное помещение"


class AdvertRooms(models.IntegerChoices):
    ONE = 1, "1 комнатная"
    TWO = 2, "2 комнатная"
    THREE = 3, "3 комнатная"
    FOUR = 4, "4 комнатная"
    FIVE = 5, "5 комнатная"
    SIX = 6, "6 комнатная"
    SEVEN = 7, "7 комнатная"


class AdvertLayout(models.TextChoices):
    STUDIO = "Студия, санузел", "Студия, санузел"
    CLASSIC = "Классическая", "Классическая"
    EURO = "Европланировка", "Европланировка"
    FREE = "Свободная", "Свободная"


class AdvertAgentCommission(models.IntegerChoices):
    SMALL = 5000, "5 000 ₴"
    MEDIUM = 15000, "15 000 ₴"
    BIG = 30000, "30 000 ₴"


class AdvertCommunication(models.TextChoices):
    CALL_MESSAGE = "Звонок + сообщение", "Звонок + сообщение"
    CALL = "Звонок", "Звонок"
    MESSAGE = "Сообщение", "Сообщение"


class AdvertCondition(models.TextChoices):
    ROUGH_FINISH = "Черновая", "Черновая"
    REPAIR_FROM_THE_DEVELOPER = (
        "Ремонт от застройщика",
        "Ремонт от застройщика",
    )
    RESIDENTIAL_CONDITION = "В жилом состоянии", "В жилом состоянии"


class Advert(models.Model):
    complex = models.ForeignKey("builder.Complex", on_delete=models.CASCADE)
    address = models.TextField()
    description = models.TextField()
    main_photo = models.ImageField(upload_to=get_timestamp_path)
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    grounds_doc = models.CharField(
        max_length=100, choices=AdvertDocument.choices
    )
    appointment = models.CharField(
        max_length=100, choices=AdvertAppointment.choices
    )
    room_count = models.CharField(max_length=100, choices=AdvertRooms.choices)
    layout = models.CharField(max_length=100, choices=AdvertLayout.choices)
    living_condition = models.CharField(
        max_length=100, choices=AdvertCondition.choices
    )
    square = models.PositiveIntegerField()
    kitchen_square = models.PositiveIntegerField()
    balcony_or_loggia = models.BooleanField()
    heating_type = models.CharField(
        max_length=100, choices=HeatingTypes.choices
    )
    payment_type = models.CharField(
        max_length=100, choices=PaymentTypes.choices
    )
    agent_commission = models.PositiveIntegerField(
        choices=AdvertAgentCommission.choices
    )
    communication_type = models.CharField(choices=AdvertCommunication.choices)
    price = models.PositiveIntegerField()
    date_published = models.DateTimeField(auto_now_add=True)
    watched_count = models.PositiveIntegerField()
    gallery = models.ForeignKey("builder.Gallery", on_delete=models.CASCADE)

    class Meta:
        db_table = "advert"


class Color(models.Model):
    title = models.CharField()

    class Meta:
        db_table = "color"


class Phrase(models.Model):
    title = models.CharField()

    class Meta:
        db_table = "phrase"


class Promotion(models.Model):
    phrase = models.BooleanField()
    highlight = models.BooleanField()
    highlight_color = models.ForeignKey(
        "Color", on_delete=models.SET_NULL, null=True
    )
    phrase_content = models.ForeignKey(
        "Phrase", on_delete=models.SET_NULL, null=True
    )
    big_advert = models.BooleanField()
    turbo = models.BooleanField()
    raise_advert = models.BooleanField()
    price = models.PositiveIntegerField()
    advert = models.OneToOneField("Advert", on_delete=models.CASCADE)

    class Meta:
        db_table = "promotion"


class Chat(models.Model):
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "chat"


class ChatMessage(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        "users.Client", on_delete=models.SET_NULL, null=True
    )
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_timestamp_path)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message"


class Subscription(models.Model):
    expiration_date = models.DateTimeField()
    auto_renewal = models.BooleanField()
    client = models.OneToOneField("users.Client", on_delete=models.CASCADE)

    class Meta:
        db_table = "subscription"


class Filter(models.Model):
    address = models.TextField()
    layout = models.CharField(max_length=100, choices=AdvertLayout.choices)
    grounds_doc = models.CharField(
        max_length=100, choices=AdvertDocument.choices
    )
    room_count = models.CharField(max_length=100, choices=AdvertRooms.choices)
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    min_square = models.PositiveIntegerField()
    max_square = models.PositiveIntegerField()
    appointment = models.CharField(
        max_length=100, choices=AdvertAppointment.choices
    )
    payment_type = models.CharField(
        max_length=100, choices=PaymentTypes.choices
    )
    condition = models.CharField(
        max_length=100, choices=AdvertCondition.choices
    )
    client = models.OneToOneField("users.Client", on_delete=models.CASCADE)

    class Meta:
        db_table = "filter"
