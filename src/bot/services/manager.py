from typing import AsyncGenerator, Dict

# from outline_vpn.outline_vpn import OutlineVPN

from src.config import vpn_config


# class OutlineManager:
#     def __init__(self):
#         self.vpn_clients = {}
#
#     async def init_vpn_clients(self,
#                                servers_info: dict,
#                                server_name: str = None
#                                ):
#         if not self.vpn_clients:
#
#             if server_name is None:
#                 self.vpn_clients = {
#                     country: OutlineVPN(api_url=vpn_config[country].api_url)
#                     for country in servers_info
#                 }
#                 for country, client in self.vpn_clients.items():
#                     await client.init(vpn_config[country].cert_sha256)
#
#             else:
#                 if server_name not in self.vpn_clients:
#                     self.vpn_clients[server_name] = OutlineVPN(api_url=vpn_config[server_name].api_url)
#                     await self.vpn_clients[server_name].init(vpn_config[server_name].cert_sha256)
#
#     async def get_clients(self,
#                           servers_info,
#                           server_id: str = None
#                           ) -> AsyncGenerator[dict[str, OutlineVPN], None]:
#         await self.init_vpn_clients(servers_info, server_id)
#         yield self.vpn_clients
#
#
# outline_manager = OutlineManager()
#
#
# async def get_vpn_clients(
#                          servers_info: dict,
#                          server_name: str = None
#                          ) -> Dict[str, OutlineVPN]:
#     async for clients in outline_manager.get_clients(servers_info, server_name):
#         print(clients)
#         return clients

# # Create a new key
# new_key = vpn_client.create_key()
#
# # Rename it
# vpn_client.rename_key(new_key.key_id, "new_key")

# # Delete it
# vpn_client.delete_key(new_key.key_id)
#
# # Set a monthly data limit for a key (20MB)
# vpn_client.add_data_limit(new_key.key_id, 1000 * 1000 * 20)
#
# # Remove the data limit
# vpn_client.delete_data_limit(new_key.key_id)
