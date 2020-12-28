from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from Classes import Invoice_class
from data import config
from loader import dp
from aiogram import types

# @dp.message_handler(text='/invoice')
from states import Test


@dp.message_handler(Command('invoice'))
async def enter_test(message: types.Message):
    await message.answer("Вы начали формирование Счета.\n"
                         "Введите Покупателя: ")

    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["answer1"] = answer
    await message.answer("Введите Продавца: ")

    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    print('@dp.message_handler(state=Test.Q2)')
    # data = await state.get_data()  # Достаем данные из машины состояний - словарь
    # answer1 = data.get("answer1")
    answer2 = message.text  # ВВЕЛИ ПРОДАВЦА
    # await message.answer(f'Покупатель: {answer1}\n'
    #                      f'Продавец: {answer2}')
    async with state.proxy() as data:
        data["answer2"] = answer2  # Занесли данные о продавце

    await message.answer("Введите название товара или услуги: ")

    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    print('@dp.message_handler(state=Test.Q3)')
    answer3 = message.text  # ВВЕЛИ НАЗВАНИЕ ТОВАРА ИЛИ УСЛУГИ
    async with state.proxy() as data:
        data["answer3"] = answer3

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}')
    await message.answer("Введите колличество товара или услуги: ")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text  # ВВЕЛИ КОЛЛИЧЕСТВО
    async with state.proxy() as data:
        data["answer4"] = answer4

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}\n'
                         f'Колличество: {answer4}')
    print('@dp.message_handler(state=Test.Q4)')
    await message.answer("Введите цену за 1 ед. изм.: ")
    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text  # ВВЕЛИ ЦЕНУ
    async with state.proxy() as data:
        data["answer5"] = answer5

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}\n'
                         f'Колличество: {answer4}\n'
                         f'Цена за 1 ед.изм.:{answer5} рублей')
    print('@dp.message_handler(state=Test.Q5)')
    await message.answer("Введите еденицу измерения (м.кв.,шт.): ")
    await Test.next()


@dp.message_handler(state=Test.Q6)
async def answer_q5(message: types.Message, state: FSMContext):
    answer6 = message.text  # ВВЕЛИ Ед.изм.
    async with state.proxy() as data:
        data["answer6"] = answer6

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")
    answer5 = data.get("answer5")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}\n'
                         f'Колличество: {answer4}\n'
                         f'Цена за 1 ед.изм.:{answer5}\n рублей'
                         f'Ед.изм.:{answer6}')
    print('@dp.message_handler(state=Test.Q6)')
    await message.answer("Счет сформирован!")

    new_Invoice = Invoice_class.Invoice(customer=answer1, executor=answer2,
                                        name_of_services=answer3, quantity=answer4,
                                        price=answer5, units=answer6)
    new_Invoice.exel_generator()

    await state.reset_state(with_data=False)  # Сбрасывает состояние но не данные


    # await state.finish() # Сбрасывается состояние и сбрасываются данные
