from typing import Dict, List, Protocol


class ThirdPartyYoutubeClass:
    def list_videos(self) -> List[int]:
        """list videos"""

    def get_video_info(self, id: int) -> Dict[str, str]:
        """return video detail"""

    def download_video(self, id: int) -> bytes:
        """download videos"""


class ThirdPartyYoutubeLib(Protocol):
    def list_videos(self) -> List[int]:
        ...

    def get_video_info(self, id: int) -> Dict[str, str]:
        ...

    def download_video(self, id: int) -> bytes:
        ...


class CachedYoutubeClass:
    def __init__(self, service: ThirdPartyYoutubeLib):
        self.service = service
        self.need_reset = False
        self.cache_list = {}
        self.video_list = {}
        self.video_info = {}

    def set_reset(self, option: bool = True) -> None:
        self.need_reset = option

    def list_videos(self) -> List[int]:
        if self.need_reset:
            return self.service.list_videos()
        return self.cache_list

    def get_video_info(self, id: int) -> Dict[str, str]:
        if self.need_reset:
            return self.video_info.get(id)
        return self.service.get_video_info(id)

    def download_video(self, id: int) -> bytes:
        if not (video := self.video_list.get(id)):
            video = self.service.download_video(id)
        return video


"""
In Proxy pattern, the actual service is overwrapped by proxy
object. The proxy object then decides whether to process on its own
or use the actual object to process.
"""


if __name__ == "__main__":
    youtube_service = ThirdPartyYoutubeClass()
    proxy = CachedYoutubeClass(youtube_service)
    proxy.set_reset()
    proxy.list_videos()
    proxy.get_video_info(100)
    proxy.set_reset(False)
    proxy.download_video(100)
