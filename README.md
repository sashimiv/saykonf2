# saykonf2
создан, для генерации пароля
## История проекта
Начал разрабатывать в январе 2023 года, так как мне надоело, что нету хороших генераторов, как говорится, лучшее это свое, поэтому я взялся за его разработку, спустя неделю проект был полностью готов

Первый полный рефакторинг был в апреле 2023 года, он заключался улучшении моментов связанных с отображением и частично была переписана обработка, заместо random стал использоваться secrets

Второй полный рефакторинг был в июне 2023 года, обратный переход на random с более понятной структурой кода

Третий полный рефакторинг произошел в феврале 2024, он полностью изменил saykonf, он стал понятнее в десятки раз, стал использоваться sqlite3 для записи паролей, логина, сервиса, в этом же рефакторинге появились и они, теперь при не указании длинны, выбирается рекомендуемая, стал использоваться ООП, все еще используется random для генерации

Следующий рефакторинг неизвестно когда будет, но планируется увеличить защиту пароля и возможно что то ещё
