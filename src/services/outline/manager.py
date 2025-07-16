from outline_vpn.outline_vpn import OutlineVPN


class OutlineManager:
    async def vpn_client_init(self, api_url: str, cert_sha256: str):
        return OutlineVPN(api_url, cert_sha256)


outline_manager = OutlineManager()
