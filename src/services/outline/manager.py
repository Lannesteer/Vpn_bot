from outline_vpn.outline_vpn import OutlineVPN

from src.config import vpn_config


class OutlineManager:
    async def vpn_client_init(self, server: str):
        client = OutlineVPN(api_url=vpn_config.get(f"{server.country}").api_url,
                            cert_sha256=vpn_config.get(f"{server.country}").cert_sha256)
        return client


outline_manager = OutlineManager()
