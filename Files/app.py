import pybase64
import base64 
import requests
import binascii
import os


def decode_base64(encoded):

    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded


def generate_v2ray_configs(decoded_data):

    configs = []

    for config in decoded_data:
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs


def decode_links(links):

    decoded_data = []

    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)

    sorted_configs = generate_v2ray_configs(decoded_data)

    return sorted_configs


def decode_dir_links(dir_links):


    decoded_dir_links = []

    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)

    return decoded_dir_links


def main():
    links = [
'https://raw.githubusercontent.com/thuhollow2/myconfig/refs/heads/main/config.yaml',
'http://141.147.161.50:12580/clash/proxies',
'http://150.230.195.209:12580/clash/proxies',
'http://155.248.172.106:12580/clash/proxies',
'http://172.245.30.41/clash.yaml',
'http://175.178.182.178:12580/clash/proxies',
'http://66.42.50.118:12580/clash/proxies',
'http://beetle.lander.work/clash/proxies',
'http://weoknow.com/data/dayupdate/1/z.txt',
'http://weoknow.com/data/dayupdate/2/z.txt',
'http://www.xrayvip.com/free.txt',
'https://chromego-sub.netlify.app/sub/merged_proxies_new.yaml',
'https://clash.221207.xyz/pubclashyaml',
'https://clashe.eu.org/clash/proxies',
'https://fragment-freevpnhomes-subscription.meshkintaj.homes',
'https://ghostcc.cc/ss.cn/cn.ovg',
'https://iwxf.netlify.app',
'https://jiang.netlify.app',
'https://miner.isherv.in',
'https://muma16fx.netlify.app',
'https://my5353.com/bmCUK',
'https://nekocandy.pages.dev/sub',
'https://proxy.crazygeeky.com/clash/proxies',
'https://proxy.fldhhhhhh.top/clash/proxies',
'https://proxypool.link/clash/proxies',
'https://proxypool.link/sip002/sub',
'https://proxypool.link/trojan/sub',
'https://proxypool.link/vmess/sub',
'https://proxypool1999.banyunxiaoxi.icu/clash/proxies',
'https://pxypool.131433.xyz/clash/proxies',
'https://shadowmere.akiel.dev/api/b64sub',
'https://sub.5112233.xyz/auto',
'https://sub.reajason.eu.org/clash.yaml',
'https://sub.xn--9sw509f.eu.org/auto',
'https://subs.zeabur.app/clash',
'https://tsutsu.top/JEmV1o5',
'https://v2ray.neocities.org/v2ray.txt',
'https://vpn.fail/free-proxy/v2ray',
'https://www.xrayvip.com/free.txt',
'https://www.xrayvip.com/free.yaml',
'https://www.youneed.win/free-ss',
'https://youlianboshi.netlify.app',
'https://yugogo.xyz/?p=1117',
'https://raw.githubusercontent.com/qjlxg/V2rayCollector/main/sub/mix',
'https://sub.sharecentre.online/sub',
'https://github.com/LalatinaHub/Mineral/raw/refs/heads/master/result/nodes',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/hysteria.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/hysteria2.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/hy2.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/ss.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/ssr.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/trojan.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/tuic.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/vless.txt',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/vmess.txt',
'https://github.com/qjlxg/hy2/raw/refs/heads/main/splitted/vmess',
'https://github.com/qjlxg/hy2/raw/refs/heads/main/splitted/vless',
'https://github.com/qjlxg/hy2/raw/refs/heads/main/splitted/trojan',
'https://github.com/qjlxg/hy2/raw/refs/heads/main/splitted/ss',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/v2',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/tr',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/ssr',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/ss',
'https://github.com/qjlxg/Ray/raw/main/config.txt',
'https://github.com/qjlxg/aggregator/raw/refs/heads/main/data/clash.yaml',
'https://github.com/qjlxg/proxy-minging/raw/refs/heads/main/v2ray.txt',
'https://github.com/qjlxg/py/raw/refs/heads/main/data/clash.yaml',
'https://github.com/qjlxg/genode/raw/refs/heads/main/public/all.txt',
'https://github.com/qjlxg/ss/raw/refs/heads/master/list.txt',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/all',
'https://github.com/qjlxg/Sub2/raw/refs/heads/main/sub/share/available',
'https://github.com/qjlxg/hy2/raw/refs/heads/main/configtg.txt',
'https://github.com/qjlxg/Ray/raw/refs/heads/main/config.txt',
'https://github.com/qjlxg/py/raw/refs/heads/main/data/v2ray.txt',
'https://github.com/coldwater-10/V2ray-Configs/raw/refs/heads/main/All_Configs_Sub.txt',
'https://raw.githubusercontent.com/m3hdio1/v2ray_sub/main/v2ray_sub.txt',
'https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_Sub.txt',
'https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt',
'https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt',
'https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes',
'https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/wenode.txt',
'https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/merged.txt',
'https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/kkzui.txt',
'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt',
'https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list_raw.txt',
'https://raw.githubusercontent.com/HakurouKen/free-node/main/public',
'https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt',
'https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt',
'https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt',
'https://raw.githubusercontent.com/asakura42/vss/master/output.txt',
 'https://mrpooya.top/api/Topfhwqqw.php',
'https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/All_Configs_Sub.txt',
'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
'https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/main/sub/Mix/mix.txt',
'https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt',
'https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/sub',
'https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/clashsub.txt',
'https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/v2raysub.txt',
'https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt',
'https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/mix',
'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt',
'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt',
'https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged',
'https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config',
'https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt',
'https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt',
'https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num',
'https://raw.githubusercontent.com/yebekhe/ConfigCollector/main/sub/mix',
'https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt',
'https://sub.pmsub.me/base64',
'https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml',
'https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/all.txt',
'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix',
'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config'

    ]
    dir_links = [
'https://raw.githubusercontent.com/shabane/kamaji/master/hub/b64/merged.txt'
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    merged_configs = decoded_links + decoded_dir_links
    output_folder = os.path.abspath(os.path.join(os.getcwd(), '..'))
    base64_folder = os.path.join(output_folder, 'Base64')

    # Delete existing output files
    filename = os.path.join(output_folder, f'All_Configs_Sub.txt')
    filename1 = os.path.join(output_folder, f'All_Configs_base64_Sub.txt')
    if os.path.exists(filename):
        os.remove(filename)
    if os.path.exists(filename1):
        os.remove(filename1)
    for i in range(20):
        filename = os.path.join(output_folder, f'Config list{i}.txt')
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f'Config list{i}_base64.txt')
        if os.path.exists(filename1):
            os.remove(filename1)

    # Remove TLS configs file
    filename = os.path.join(output_folder, f'Config_TLS.txt')
    if os.path.exists(filename):
        os.remove(filename)

    # Write merged configs to output file
    output_file = os.path.join(output_folder, 'All_Configs_Sub.txt')
    with open(output_file, 'w') as f:
        for config in merged_configs:
            f.write(config + '\n')

    # Split merged configs into files with no more than 1000 configs per file
    with open(output_file, 'r') as f:
        lines = f.readlines()
    num_lines = len(lines)
    max_lines_per_file = 3680
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file
    for i in range(num_files):
        start_index = i * max_lines_per_file
        end_index = (i + 1) * max_lines_per_file
        filename = os.path.join(output_folder, f'Config list{i+1}.txt')
        with open(filename, 'w') as f:
            for line in lines[start_index:end_index]:
                f.write(line)
                
    # Encode to base64 and save merged configs to a single file
    encoded_merged_configs = base64.b64encode("\n".join(merged_configs).encode()).decode()
    output_file = os.path.join(output_folder, 'All_Configs_base64_Sub.txt')
    with open(output_file, 'w') as f:
        f.write(encoded_merged_configs)

    # Encode and save each Sub{i+1}.txt file to base64_folder as Sub{i+1}_base64.txt
    for i in range(num_files):
        input_filename = os.path.join(output_folder, f'Config list{i+1}.txt')
        output_filename = os.path.join(base64_folder, f'Config list{i+1}_base64.txt')

        with open(input_filename, 'r') as input_file:
            config_data = input_file.read()
        
        encoded_config = base64.b64encode(config_data.encode()).decode()

        with open(output_filename, 'w') as output_file:
            output_file.write(encoded_config)

    # Take all tls enabled configs and save them to Configs_TLS.txt
    tls_file = os.path.join(output_folder, f"Configs_TLS.txt")
    with open(tls_file, "w") as f:
        for line in lines:
            if "security=tls" in line:
                f.write(line)

    # Take all tls enabled configs from tls_file, encode and save them to Configs_TLS_base64.txt
    tls_encoded_file = os.path.join(output_folder, f'Config_TLS_base64.txt')
    with open(tls_file, 'r') as input_file:
        tls_config_data = input_file.read()
    
    encoded_tls_config = base64.b64encode(tls_config_data.encode()).decode()

    with open(tls_encoded_file, 'w') as output_file:
        output_file.write(encoded_tls_config)

    
if __name__ == "__main__":
    main()
