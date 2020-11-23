from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import subprocess

class FlamshotExtension(Extension):

    def __init__(self):
        super(FlamshotExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_argument()
        items = [
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="Flameshot",
                    description="Screenshot using Flameshot",
                    on_enter=ExtensionCustomAction(data),
                    ),
                ]

        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        subprocess.Popen("flameshot gui --delay 200", shell=True)

        return RenderResultListAction([])

if __name__ == '__main__':
    FlamshotExtension().run()