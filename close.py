from plyer import notification

game = "Rocket League"
notification.notify(
    title = "ERROR:削除できませんでした。",
    message = "{}が起動していません。".format(game),
    app_name = "Deleter",
    timeout = 5
)