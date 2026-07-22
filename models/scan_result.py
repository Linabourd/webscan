class ScanResult:
    def __init__(self) -> None:
        self.findings = []

    def add_finding(self, finding: dict) -> None:
        self.findings.append(finding)
