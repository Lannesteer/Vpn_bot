from outline_vpn.outline_vpn import OutlineVPN

from src.config import vpn_config


class OutlineManager:
    def __init__(self):
        self.api_url = None
        self.cert_sha256 = None

    async def get_vpn_client(self, server_info):
        return OutlineVPN(self.api_url, self.cert_sha256)


outline_manager = OutlineManager()
