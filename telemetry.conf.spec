#   Version 6.6.4
#
# This file contains possible attributes and values for configuring global
# telemetry settings. Please note that enabling these settings would enable
# apps to collect telemetry data about app usage and other properties.
#
# There is no global, default telemetry.conf. Instead, a telemetry.conf may
# exist in each app in Splunk Enterprise.
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#  * You can also define global settings outside of any stanza, at the top
#    of the file.
#  * Each conf file should have at most one default stanza. If there are
#    multiple default stanzas, attributes are combined. In the case of
#    multiple definitions of the same attribute, the last definition in the
#    file wins.
#  * If an attribute is defined at both the global level and in a specific
#    stanza, the value in the specific stanza takes precedence.

[general]
optInVersion = <number>
* An integer that identifies the set of telemetry data to be collected
* Incremented upon installation if the data set collected by Splunk has changed
* This field was introduced for version 2 of the telemetry data set. So,
  when this field is missing, version 1 is assumed.
* Should not be changed manually

optInVersionAcknowledged = <number>
* The latest optInVersion acknowledged by a user on this deployment
* While this value is less than the current optInVersion, a prompt for
  data collection opt-in will be shown to users with the
  edit_telemetry_settings capability at login
* Once a user confirms interaction with this login - regardless of
  opt-in choice - this number will be set to the value of optInVersion
* This gets set regardless of whether the user opts in using the opt-in
  dialog or the Settings > Instrumentation page
* Unset by default

sendLicenseUsage = true|false
* Send the licensing usage information of splunk/app to the app owner
* Defaults to false

sendAnonymizedUsage = true|false
* Send the anonymized usage information about various categories like
  infrastructure, utilization etc of splunk/app to the app owner
* Defaults to false

sendAnonymizedWebAnalytics = true|false
* Send the anonymized usage information about user interaction with
  splunk performed through the web UI
* Defaults to false

precheckSendLicenseUsage = true|false
* Default value for sending license usage in opt in modal
* Defaults to true

precheckSendAnonymizedUsage = true|false
* Default value for sending anonymized usage in opt in modal
* Defaults to false

showOptInModal = true|false
* DEPRECATED - see optInVersion and optInVersionAcknowledged settings
* Shows the opt in modal. DO NOT SET! When a user opts in, it will
  automatically be set to false to not show the modal again.
* Defaults to true

deploymentID = <string>
* A uuid used to correlate telemetry data for a single splunk
  deployment over time. The value is generated the first time
  a user opts in to sharing telemetry data.

deprecatedConfig = true|false
* Setting to determine whether the splunk deployment is following
  best practices for the platform as well as the app
* Defaults to false

retryTransaction = <string>
* Setting that is created if the telemetry conf updates cannot be delivered to
  the cluster master for the splunk_instrumentation app.
* Defaults to an empty string

swaEndpoint = <string>
* The URL to which swajs will forward UI analytics events
* If blank, swajs sends events to the Splunk MINT CDS endpoint.
* Blank by default

telemetrySalt = <string>
* A salt used to hash certain fields before transmission
* Autogenerated as a random UUID when splunk starts
