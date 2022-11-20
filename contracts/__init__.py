from extras.plugins import PluginConfig

class ContractsConfig(PluginConfig):
    name = 'contracts'
    verbose_name = 'Contracts'
    description = 'Contract management NetBox plugin'
    version = '0.1'
    author = 'Marc Lebreuil'
    author_email = 'marc@famillelebreuil.net'
    base_url = 'contracts'
    required_settings = []
    default_settings = {
    }

config = ContractsConfig
