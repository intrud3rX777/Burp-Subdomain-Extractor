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
        menuList.add(swing.JMenuItem("Extract Subdomains (by root name)", actionPerformed=self.extractSubdomainsByRoot))
        return menuList

    def extractSubdomainsByRoot(self, event):
        root_input = swing.JOptionPane.showInputDialog("Enter root domain name (e.g., example):")
        if not root_input:
            return

        root_input = root_input.strip().lower()
        if not re.match(r'^[a-z0-9-]+$', root_input):
            swing.JOptionPane.showMessageDialog(None, "Invalid root domain name.")
            return

        http_messages = self._invocation.getSelectedMessages()
        extracted_subdomains = set()

        # Match domains like a.example.com, b.api.example.org, etc.
        domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+(?:' + re.escape(root_input) + r')\.[a-z]{2,}\b'
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
            swing.JOptionPane.showMessageDialog(None, "No matching subdomains found for '{}'.".format(root_input))

    def copyToClipboard(self, text):
        stringSelection = StringSelection(text)
        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(stringSelection, None)
