#   Version 8.2.0
#
# This file contains possible setting/value pairs for configuring Windows
# Management Instrumentation (WMI) access from Splunk Enterprise.
#
# There is a wmi.conf in $SPLUNK_HOME\etc\system\default\.  To set custom
# configurations, place a wmi.conf in $SPLUNK_HOME\etc\system\local\. For
# examples, see wmi.conf.example.
#
# You must restart Splunk Enterprise to enable configurations.
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

###################################################################
#----GLOBAL SETTINGS-----
 ###################################################################

[settings]
* Specifies parameters for the WMI input.
* The entire stanza and every parameter within it is optional.
* If the stanza is missing, Splunk Enterprise assumes system defaults.

initial_backoff = <integer>
* How long, in seconds, to wait before retrying the connection to
  the WMI provider after the first connection error.
* If connection errors continue, the wait time doubles until it reaches
  the integer specified in 'max_backoff'.
* Default: 5

max_backoff = <integer>
* How long, in seconds, to attempt to reconnect to the
  WMI provider.
* Default: 20

max_retries_at_max_backoff = <integer>
* When the WMI input has connection errors to the WMI provider, it
  backs off connection attempts by doubling the amount of time it
  waits between connection attempts. It modifies attempts from an initial interval of
  'initial_backoff' seconds to an interval specified 'max_backoff'
  seconds.
* After the input has waited 'max_backoff' seconds between connection
  attempts, and while connection errors persist, this setting tells
  the input how many times it should continue trying to connect at
  the 'max_backoff' interval.
* If reconnection to the WMI provider fails after 'max_retries' attempts,
  the input gives up and does not attempt further connections until
  you restart Splunk Enterprise.
* Default: 2

checkpoint_sync_interval = <integer>
* How long, in seconds, to wait for state data (event log checkpoint)
  to be written to disk.
* Default: 2

###################################################################
#----INPUT-SPECIFIC SETTINGS-----
###################################################################

[WMI:<name>]
* There are two types of WMI input stanza:
  * Event log stanza: Used to collect Windows Event Logs. You must configure the
    'event_log_file' setting.
  * Windows Query Language (WQL): Used to issue raw Windows Query Language (WQL)
    requests. You must configure the 'wql' setting.
* Do not use both the 'event_log_file' amd 'wql' attributes. Use one or the other.

server = <comma-separated strings>
* A comma-separated list of WMI providers (Windows machines) from which to get data.
* Default: the local machine

interval = <integer>
* How often, in seconds, to poll the WMI provider for new data.
* You must supply this setting. No default is supplied and the input does not run if the setting is
  not specified.
* No default.

disabled = <boolean>
* Whether or not the input is enabled.
* Set to 1 to disable the input, 0 to enable it.
* Default: 0 (enabled).

hostname = <string>
* All results generated by this stanza will appear to have arrived from
  the string you specify here.
* This setting is optional.
* Default: input detects the host automatically

current_only = <boolean>
* Changes the characteristics and interaction of WMI-based event
  collections.
* When you set 'current_only' to 1:
  * For event log stanzas, captures events that occur
    only while Splunk Enterprise is running.
  * For WQL stanzas, the input expects event notification queries. The
    WMI class you query must support sending events. Failure to supply
    the correct event notification query structure causes WMI to return
    a syntax error to the input.
  * An example event notification query that watches for process creation:
    * SELECT * FROM __InstanceCreationEvent WITHIN 1 WHERE
      TargetInstance ISA 'Win32_Process'.
* When you set 'current_only' to 0:
  * For event log stanzas, Splunk Enterprise gathers all the events from
    the checkpoint. If there is no checkpoint, Splunk Enterprise retrieves
    all events starting from the oldest.
  * For WQL stanzas, Splunk Enterprise executes the query and retrieves
    the results. The query is a non-notification query.
  * For example
    * Select * Win32_Process where caption = "explorer.exe"
* Default: 0

use_old_eventlog_api = <boolean>
* Whether or not to read Event Log events with the Event Logging API rather
  than the Windows Event Log API.
* This is an advanced setting. Contact Splunk Support before you change it.
* If set to "true", the input uses the Event Logging API (instead of the Windows Event Log API)
  to read from the Event Log on Windows Server 2008, Windows Vista, and later installations.
* Default: false (Use the API that is specific to the OS.)

use_threads = <integer>
* The number of threads, in addition to the default writer thread, that can
  be created to filter events with the deny list or allow list regular expression.
* This is an advanced setting. Contact Splunk Support before you change it.
* The maximum number of threads is 15.
* Default: 0

thread_wait_time_msec = <integer>
* The interval, in milliseconds, between attempts to re-read Event Log files when a read error occurs.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: 5000

suppress_checkpoint = <boolean>
* Whether or not the Event Log strictly follows the 'checkpointInterval' setting when it saves a checkpoint.
* By default, the Event Log input saves a checkpoint from between zero and 'checkpointInterval' seconds,
  depending on incoming event volume.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

suppress_sourcename = <boolean>
* Whether or not to exclude the 'sourcename' field from events.
* When set to "true", the input excludes the 'sourcename' field from events and throughput performance
  (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

suppress_keywords = <boolean>
* Whether or not to exclude the 'keywords' field from events.
* When set to "true", the input excludes the 'keywords' field from events and throughput performance
  (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

suppress_type = <boolean>
* Whether or not to exclude the 'type' field from events.
* When set to true, the input excludes the 'type' field from events and throughput performance
  (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

suppress_task = <boolean>
* Whether or not to exclude the 'task' field from events.
* When set to "true", the input excludes the 'task' field from events and thruput performance
  (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

suppress_opcode = <boolean>
* Whether or not to exclude the 'opcode' field from events.
* When set to "true", the input excludes the 'opcode' field from events and throughput performance
  (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Default: false

batch_size = <integer>
* Number of events to fetch on each query.
* Default: 10

checkpointInterval = <integer>
* How often, in seconds, that the Windows Event Log input saves a checkpoint.
* Checkpoints store the event ID of acquired events. This lets the input
  continue monitoring at the correct event after a shutdown or outage.
* Default: 0

index = <string>
* Specifies the index that this input should send the data to.
* This setting is optional.
* When you define 'index', the input prepends "index=" to <string>.
* Default: "index=main" (or whatever you have set as your default index).

#####
# Event log-specific attributes:
#####

event_log_file = <string> <Application, System, etc>
* Tells the input to expect event log data for this stanza, and specifies
  the event log channels you want the input to monitor.
* To specify Event Log sources, use this setting instead of WQL.
* Specify one or more event log channels to poll. You must separate multiple
  Event Log channels with commas.
  * For exmaple, to include the Application and System channels, specify "Application, System".
* No default.

disable_hostname_normalization = <boolean>
* Whether or not the WMI input normalizes hostnames from 'localhost' to
  what is present in the %COMPUTERNAME% Windows system variable.
* If set to "true", hostname normalization is disabled.
* If set to "false" or not set, the input converts the hostname for
  'localhost' to %COMPUTERNAME%.
* 'localhost' refers to the following list of strings:
  * localhost
  * 127.0.0.1
  * ::1
  * the name of the DNS domain for the local computer
  * the fully qualified DNS name
  * the NetBIOS name
  * the DNS host name of the local computer

#####
# WQL-specific attributes:
#####

wql = <string>
* Configures the WMI input to expect data from a WMI provider for this stanza, and
  specifies the Windows Query Language query you want the input to make to
  gather that data.
* Use this if you are not using the 'event_log_file' setting.
* Ensure that your WQL queries have the correct syntax and structure when you
  use this option.
  * For example,
    SELECT * FROM Win32_PerfFormattedData_PerfProc_Process WHERE Name = "splunkd".
* If you want to use event notification queries, you must also set the
  "current_only" attribute to "1" within the stanza, and your query must be
  appropriately structured for event notification (meaning its WQL string
  must contain one or more of the GROUP, WITHIN or HAVING clauses.)
  * For example,
    SELECT * FROM __InstanceCreationEvent WITHIN 1 WHERE TargetInstance ISA
    'Win32_Process'
* No default.

namespace = <string>
* The namespace where the WMI provider resides.
* The namespace specification can either be relative (root\cimv2) or absolute
  (\\server\root\cimv2).
* If the server attribute is present, you cannot specify an absolute
  namespace.
* Default: root\cimv2.
