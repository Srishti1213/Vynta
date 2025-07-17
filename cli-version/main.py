# main.py - Full Suite Trigger
from modules import (
    hidden_apps, permission_audit, sms_call_log,
    file_audit, adb_history, gps_timeline, whois_lookup,
    dns_check, port_scanner, social_detector, email_validator,
    traceroute_map, protocol_detector, ssl_cert_check, bandwidth_analyzer
)

if __name__ == '__main__':
    print("\n[📱 Android Analysis Suite v4 - Running All Modules]\n")

    hidden_apps.check_hidden_apps("samples/sample_applist.txt")
    permission_audit.audit_permissions("samples/sample_permissions.txt")
    sms_call_log.scan_sms_calls("samples/sample_sms_call_log.txt")
    file_audit.find_exfil_paths("samples/sample_filesystem.txt")
    adb_history.check_adb_commands("samples/sample_adb_log.txt")
    gps_timeline.extract_gps_movement("samples/sample_location.csv")
    whois_lookup.check_domain_owner("samples/dns.txt")
    dns_check.resolve_dns("samples/sample_dns.txt")
    port_scanner.scan_ports("samples/sample_portscan.txt")
    protocol_detector.detect_unusual_protocols("samples/sample_protocol_log.txt")
    ssl_cert_check.analyze_cert("samples/sample_ssl_cert.txt")
    bandwidth_analyzer.detect_anomalies("samples/sample_bandwidth.csv")
    traceroute_map.map_route("samples/sample_traceroute.txt")
    email_validator.analyze_email_headers("samples/sample_email_headers.txt")
    social_detector.detect_social_engineering("samples/sample_phishing_message.txt")
