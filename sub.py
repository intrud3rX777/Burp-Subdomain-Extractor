from burp import IBurpExtender, IContextMenuFactory
from javax import swing
from java.util import ArrayList
from java.awt import Toolkit
from java.awt.datatransfer import StringSelection
import re

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Subdomain Extractor")
        callbacks.registerContextMenuFactory(self)
        print("Subdomain Extractor extension loaded")

    def createMenuItems(self, invocation):
        self._invocation = invocation
        menuList = ArrayList()
        menuList.add(swing.JMenuItem("Extract Subdomains (by domain)", actionPerformed=self.extractSubdomainsByDomain))
        return menuList

    def extractSubdomainsByDomain(self, event):
        domain_input = swing.JOptionPane.showInputDialog("Enter domain to filter subdomains (e.g., example.com):")
        if not domain_input:
            return

        domain_input = domain_input.strip().lower()
        if not re.match(r'^[a-z0-9.-]+\.[a-z]{2,}$', domain_input):
            swing.JOptionPane.showMessageDialog(None, "Invalid domain format.")
            return

        http_messages = self._invocation.getSelectedMessages()
        extracted_subdomains = set()

        domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+' + re.escape(domain_input) + r'\b'
        unwanted_extensions = ('.js', '.css', '.scss', '.map', '.ts', '.jsx', '.json')

        for message in http_messages:
            response = message.getResponse()
            if response:
                response_str = self._helpers.bytesToString(response)
                matches = re.findall(domain_pattern, response_str)

                for domain in matches:
                    domain_lower = domain.lower()
                    if domain_lower.endswith(unwanted_extensions):
                        continue
                    if re.match(r'^[a-z]\.[a-z]', domain_lower):
                        continue
                    extracted_subdomains.add(domain_lower)

        if extracted_subdomains:
            output = "\n".join(sorted(extracted_subdomains))
            self.copyToClipboard(output)
            swing.JOptionPane.showMessageDialog(None, "{} subdomains copied to clipboard!".format(len(extracted_subdomains)))
            print("Filtered subdomains:\n" + output)
        else:
            swing.JOptionPane.showMessageDialog(None, "No matching subdomains found for '{}'.".format(domain_input))

    def copyToClipboard(self, text):
        stringSelection = StringSelection(text)
        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(stringSelection, None)
