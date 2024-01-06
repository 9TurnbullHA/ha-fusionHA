""" fetch.py """

import os
import json

output = {}

TRANSLATIONS = "/usr/local/lib/python3.11/site-packages/hass_frontend/static/translations"
COMPONENTS = "/usr/src/homeassistant/homeassistant/components"


def process_dir(_dir, _output, _keys):
    """func"""
    for filename in os.listdir(_dir):
        if filename.endswith(".json") and not filename.startswith("test"):
            _code = filename.rsplit("-", 1)[0].replace(".json", "")
            with open(os.path.join(_dir, filename), encoding="utf-8") as file:
                data = json.load(file)
                if _code not in _output:
                    _output[_code] = {}
                for _key, value_path in _keys:
                    value = data
                    for path_item in value_path:
                        if path_item in value:
                            value = value[path_item]
                        else:
                            value = None
                            break
                    if value is not None:
                        _output[_code][_key] = value


dir_keys = [
    (  # TRANSLATIONS
        TRANSLATIONS,
        [
            ("unknown", ["state.default.unknown"]),
            ("unavailable", ["state.default.unavailable"]),
            ("nothing_found", ["ui.dialogs.quick-bar.nothing_found"]),
            ("entity_not_found", ["ui.card.tile.not_found"]),
            ("delete", ["ui.common.delete"]),
            ("settings", ["panel.config"]),
            ("cancel", ["ui.card.script.cancel"]),
            ("hide", ["ui.common.hide"]),
            ("icon", ["ui.dialogs.entity_registry.editor.icon"]),
            ("name", ["ui.components.area-picker.add_dialog.name"]),
            ("remove", ["ui.common.remove"]),
            ("ok", ["ui.common.ok"]),
            ("options", ["ui.dialogs.helper_settings.input_select.options"]),
            ("date", ["ui.dialogs.helper_settings.input_datetime.date"]),
            ("done", ["ui.sidebar.done"]),
            ("say", ["ui.components.media-browser.tts.action_play"]),
            ("max", ["ui.dialogs.helper_settings.input_text.max"]),
            ("min", ["ui.dialogs.helper_settings.input_text.min"]),
            ("summary", ["ui.components.calendar.event.summary"]),
            ("yes", ["ui.common.yes"]),
            ("no", ["ui.common.no"]),
            ("brightness", ["ui.card.light.brightness"]),
            ("change_color", ["ui.dialogs.more_info_control.light.color_picker.title"]),
            ("color", ["ui.dialogs.more_info_control.light.color_picker.mode.color"]),
            ("color_temp", ["ui.dialogs.more_info_control.light.color_picker.mode.color_temp"]),
            ("toggle", ["ui.dialogs.more_info_control.light.toggle"]),
            ("menu", ["ui.common.menu"]),
            ("successfully_saved", ["ui.common.successfully_saved"]),
            ("overview", ["panel.states"]),
            ("visible", ["ui.dialogs.entity_registry.editor.visible_label"]),
            ("key_missing", ["ui.errors.config.key_missing"]),
            ("error", ["state_badge.default.error"]),
            ("history", ["panel.history"]),
            ("connection_lost", ["ui.notification_toast.connection_lost"]),
            ("connection_starting", ["ui.notification_toast.starting"]),
            ("connection_started", ["ui.notification_toast.started"]),
            ("no_options", ["ui.dialogs.helper_settings.input_select.no_options"]),
            ("forward", ["ui.card.fan.forward"]),
            ("undo", ["ui.common.undo"]),
            ("start", ["ui.card.timer.actions.start"]),
            ("pause", ["ui.card.timer.actions.pause"]),
            ("finish", ["ui.card.timer.actions.finish"]),
            ("duration", ["ui.dialogs.helper_settings.timer.duration"]),
            ("motion", ["ui.dialogs.entity_registry.editor.device_classes.binary_sensor.motion"]),
            ("copied", ["ui.common.copied"]),
            ("object", ["ui.components.selectors.selector.types.object"]),
            ("state", ["ui.components.entity.entity-state-picker.state"]),
            ("position", ["ui.card.cover.position"]),
            ("open_cover", ["ui.card.cover.open_cover"]),
            ("close_cover", ["ui.card.cover.close_cover"]),
            ("stop_cover", ["ui.card.cover.stop_cover"]),
            ("tilt_position", ["ui.card.cover.tilt_position"]),
            ("open_tilt_cover", ["ui.card.cover.open_tilt_cover"]),
            ("close_tilt_cover", ["ui.card.cover.close_tilt_cover"]),
            ("add", ["ui.common.add"]),
        ],
    ),
    (  # MEDIA_PLAYER
        f"{COMPONENTS}/media_player/translations/",
        [
            ("playing", ["entity_component", "_", "state", "playing"]),
            ("paused", ["entity_component", "_", "state", "paused"]),
            ("idle", ["entity_component", "_", "state", "idle"]),
            ("standby", ["entity_component", "_", "state", "standby"]),
            ("buffering", ["entity_component", "_", "state", "buffering"]),
            ("source", ["entity_component", "_", "state_attributes", "source", "name"]),
            ("volume_level", ["entity_component", "_", "state_attributes", "volume_level", "name"]),
        ],
    ),
    (  # CAMERA
        f"{COMPONENTS}/camera/translations/",
        [
            ("camera", ["title"]),
        ],
    ),
    (  # SWITCH
        f"{COMPONENTS}/switch/translations/",
        [
            ("on", ["entity_component", "_", "state", "on"]),
            ("off", ["entity_component", "_", "state", "off"]),
        ],
    ),
    (  # ALARM_CONTROL_PANEL
        f"{COMPONENTS}/alarm_control_panel/translations/",
        [
            ("armed", ["entity_component", "_", "state", "armed"]),
            ("armed_away", ["entity_component", "_", "state", "armed_away"]),
            ("armed_custom_bypass", ["entity_component", "_", "state", "armed_custom_bypass"]),
            ("armed_home", ["entity_component", "_", "state", "armed_home"]),
            ("armed_night", ["entity_component", "_", "state", "armed_night"]),
            ("armed_vacation", ["entity_component", "_", "state", "armed_vacation"]),
            ("arming", ["entity_component", "_", "state", "arming"]),
            ("disarmed", ["entity_component", "_", "state", "disarmed"]),
            ("disarming", ["entity_component", "_", "state", "disarming"]),
            ("pending", ["entity_component", "_", "state", "pending"]),
            ("triggered", ["entity_component", "_", "state", "triggered"]),
        ],
    ),
    (  # SUN
        f"{COMPONENTS}/sun/translations/",
        [
            ("above_horizon", ["entity_component", "_", "state", "above_horizon"]),
            ("below_horizon", ["entity_component", "_", "state", "below_horizon"]),
        ],
    ),
    (  # LOCK
        f"{COMPONENTS}/lock/translations/",
        [
            ("jammed", ["entity_component", "_", "state", "jammed"]),
            ("locked", ["entity_component", "_", "state", "locked"]),
            ("locking", ["entity_component", "_", "state", "locking"]),
            ("unlocked", ["entity_component", "_", "state", "unlocked"]),
            ("unlocking", ["entity_component", "_", "state", "unlocking"]),
        ],
    ),
    (  # COVER
        f"{COMPONENTS}/cover/translations/",
        [
            ("closed", ["entity_component", "_", "state", "closed"]),
            ("closing", ["entity_component", "_", "state", "closing"]),
            ("open", ["entity_component", "_", "state", "open"]),
            ("opening", ["entity_component", "_", "state", "opening"]),
            ("stopped", ["entity_component", "_", "state", "stopped"]),
        ],
    ),
    (  # WEATHER
        f"{COMPONENTS}/weather/translations",
        [
            ("weather", ["title"]),
            ("weather_clear_night", ["entity_component", "_", "state", "clear-night"]),
            ("weather_cloudy", ["entity_component", "_", "state", "cloudy"]),
            ("weather_exceptional", ["entity_component", "_", "state", "exceptional"]),
            ("weather_fog", ["entity_component", "_", "state", "fog"]),
            ("weather_hail", ["entity_component", "_", "state", "hail"]),
            ("weather_lightning", ["entity_component", "_", "state", "lightning"]),
            ("weather_lightning_rainy", ["entity_component", "_", "state", "lightning-rainy"]),
            ("weather_partlycloudy", ["entity_component", "_", "state", "partlycloudy"]),
            ("weather_pouring", ["entity_component", "_", "state", "pouring"]),
            ("weather_rainy", ["entity_component", "_", "state", "rainy"]),
            ("weather_snowy", ["entity_component", "_", "state", "snowy"]),
            ("weather_snowy_rainy", ["entity_component", "_", "state", "snowy-rainy"]),
            ("weather_sunny", ["entity_component", "_", "state", "sunny"]),
            ("weather_windy", ["entity_component", "_", "state", "windy"]),
            ("weather_windy_variant", ["entity_component", "_", "state", "windy-variant"]),
        ],
    ),
    (  # CLIMATE
        f"{COMPONENTS}/climate/translations/",
        [
            ("heat", ["entity_component", "_", "state", "heat"]),
            ("cool", ["entity_component", "_", "state", "cool"]),
            ("heat_cool", ["entity_component", "_", "state", "heat_cool"]),
            ("auto", ["entity_component", "_", "state", "auto"]),
            ("dry", ["entity_component", "_", "state", "dry"]),
            ("fan_only", ["entity_component", "_", "state", "fan_only"]),
            ("fan_modes", ["entity_component", "_", "state_attributes", "fan_modes", "name"]),
            ("hvac_modes", ["entity_component", "_", "state_attributes", "hvac_modes", "name"]),
            ("target_temperature", ["entity_component", "_", "state_attributes", "temperature", "name"]),
            ("swing_modes", ["entity_component", "_", "state_attributes", "swing_modes", "name"]),
            ("low", ["entity_component", "_", "state_attributes", "fan_mode", "state", "low"]),
            ("medium", ["entity_component", "_", "state_attributes", "fan_mode", "state", "medium"]),
            ("high", ["entity_component", "_", "state_attributes", "fan_mode", "state", "high"]),
            ("heating", ["entity_component", "_", "state_attributes", "hvac_action", "state", "heating"]),
            ("cooling", ["entity_component", "_", "state_attributes", "hvac_action", "state", "cooling"]),
            ("fan", ["entity_component", "_", "state_attributes", "hvac_action", "state", "fan"]),
            ("drying", ["entity_component", "_", "state_attributes", "hvac_action", "state", "drying"]),
        ],
    ),
    (  # DEVICE_TRACKER
        f"{COMPONENTS}/device_tracker/translations/",
        [
            ("home", ["entity_component", "_", "state", "home"]),
            ("not_home", ["entity_component", "_", "state", "not_home"]),
        ],
    ),
    (  # PROFILE
        f"{TRANSLATIONS}/profile",
        [
            ("language", ["ui.panel.profile.language.header"]),
            ("token", ["ui.panel.profile.long_lived_access_tokens.header"]),
            ("log_out", ["ui.panel.profile.logout"]),
            ("theme", ["ui.panel.profile.themes.header"]),
            ("time_format_header", ["ui.panel.profile.time_format.header"]),
            ("time_format_12", ["ui.panel.profile.time_format.formats.12"]),
            ("time_format_24", ["ui.panel.profile.time_format.formats.24"]),
            ("time_format_auto", ["ui.panel.profile.time_format.formats.language"]),
            ("time_format_description", ["ui.panel.profile.time_format.description"]),
            ("none", ["ui.panel.profile.number_format.formats.none"]),
            ("confirm_log_out", ["ui.panel.profile.logout_text"]),
        ],
    ),
    (  # CONFIG
        f"{TRANSLATIONS}/config",
        [
            ("ha_url", ["ui.panel.config.url.caption"]),
            ("save", ["ui.panel.config.automation.editor.save"]),
            ("status", ["ui.panel.config.entities.picker.headers.status"]),
            ("docs", ["ui.panel.config.info.documentation"]),
            ("url", ["ui.panel.config.lovelace.resources.detail.url"]),
            ("addons", ["ui.panel.config.dashboard.supervisor.main"]),
            ("discovered", ["ui.panel.config.integrations.discovered"]),
            ("show", ["ui.panel.config.integrations.disable.show"]),
            ("auth", ["ui.panel.config.application_credentials.caption"]),
            ("preview", ["ui.panel.config.blueprint.add.import_btn"]),
            ("time", ["ui.panel.config.automation.editor.triggers.type.time.label"]),
            ("nothing_configured", ["ui.panel.config.integrations.none"]),
            ("show_in_sidebar", ["ui.panel.config.lovelace.dashboards.picker.headers.sidebar"]),
            ("hours", ["ui.panel.config.automation.editor.triggers.type.time_pattern.hours"]),
            ("minutes", ["ui.panel.config.automation.editor.triggers.type.time_pattern.minutes"]),
            ("seconds", ["ui.panel.config.automation.editor.triggers.type.time_pattern.seconds"]),
            ("numeric", ["ui.panel.config.automation.editor.triggers.type.numeric_state.label"]),
            ("template", ["ui.panel.config.automation.editor.triggers.type.template.label"]),
            ("before", ["ui.panel.config.automation.editor.triggers.type.calendar.before"]),
            ("after", ["ui.panel.config.automation.editor.triggers.type.calendar.after"]),
            ("date_or_time", ["ui.panel.config.helpers.types.input_datetime"]),
            ("code", ["ui.panel.config.automation.editor.actions.type.device_id.extra_fields.code"]),
            ("value", ["ui.panel.config.automation.editor.actions.type.device_id.extra_fields.value"]),
            ("shortcuts", ["ui.panel.config.zha.configuration_page.shortcuts_title"]),
            ("group", ["ui.panel.config.users.editor.group"]),
            ("hidden", ["ui.panel.config.devices.entities.hidden"]),
            ("script", ["ui.panel.config.blueprint.overview.types.script"]),
            ("size", ["ui.panel.config.backup.size"]),
            ("timer", ["ui.panel.config.helpers.types.timer"]),
            ("javascript_module", ["ui.panel.config.lovelace.resources.types.module"]),
            ("copy", ["ui.panel.config.repairs.copy"]),
            ("media", ["ui.panel.config.storage.network_mounts.mount_usage.media"]),
            ("service", ["ui.panel.config.devices.type.service_heading"]),
        ],
    ),
    (  # ONBOARDING
        f"{TRANSLATIONS}/page-onboarding",
        [
            ("detect", ["ui.panel.page-onboarding.core-config.button_detect"]),
        ],
    ),
    (  # LOVELACE
        f"{TRANSLATIONS}/lovelace",
        [
            ("suggestion", ["ui.panel.lovelace.editor.suggest_card.header"]),
            ("search", ["ui.panel.lovelace.editor.card.generic.search"]),
            ("edit", ["ui.panel.lovelace.editor.edit_card.edit"]),
            ("raw", ["ui.panel.lovelace.editor.menu.raw_editor"]),
            ("exit_edit_mode", ["ui.panel.lovelace.menu.exit_edit_mode"]),
            ("unsaved_changes", ["ui.panel.lovelace.editor.raw_editor.confirm_unsaved_changes"]),
            ("edit_title", ["ui.panel.lovelace.editor.edit_lovelace.edit_title"]),
            ("section", ["ui.panel.lovelace.editor.card.entities.entity_row.section"]),
            ("button", ["ui.panel.lovelace.editor.card.entities.entity_row.button"]),
            ("sidebar", ["ui.panel.lovelace.editor.edit_view.types.sidebar"]),
            ("sensor", ["ui.panel.lovelace.editor.card.sensor.name"]),
            ("card_configuration", ["ui.panel.lovelace.editor.edit_card.header"]),
            ("change_type", ["ui.panel.lovelace.editor.card.conditional.change_type"]),
            ("day", ["ui.panel.lovelace.editor.card.calendar.views.dayGridDay"]),
            ("month", ["ui.panel.lovelace.editor.card.calendar.views.dayGridMonth"]),
            ("invalid_timestamp", ["ui.panel.lovelace.components.timestamp-display.invalid"]),
            ("divider", ["ui.panel.lovelace.editor.card.entities.entity_row.divider"]),
            ("unsaved_changes_title", ["ui.panel.lovelace.editor.raw_editor.unsaved_changes"]),
            ("confirm_delete_message", ["ui.panel.lovelace.views.confirm_delete_existing_cards_text"]),
            ("add_view", ["ui.panel.lovelace.editor.edit_view.add"]),
            ("edit_view", ["ui.panel.lovelace.editor.edit_view.edit"]),
            ("edit_yaml", ["ui.panel.lovelace.editor.edit_view.edit_yaml"]),
            ("error_save_yaml", ["ui.panel.lovelace.editor.raw_editor.error_save_yaml"]),
            ("navigate", ["ui.panel.lovelace.editor.action-editor.actions.navigate"]),
            ("appearance", ["ui.panel.lovelace.editor.card.tile.appearance"]),
            ("visibility", ["ui.panel.lovelace.editor.edit_view.tab_visibility"]),
            ("edit_ui", ["ui.panel.lovelace.editor.header"]),
            ("graph", ["ui.panel.lovelace.editor.header-footer.types.graph.name"]),
            ("loading", ["ui.panel.lovelace.cards.energy.loading"]),
            ("period", ["ui.panel.lovelace.editor.card.statistics-graph.period"]),
            ("period_hour", ["ui.panel.lovelace.editor.card.statistics-graph.periods.hour"]),
            ("period_day", ["ui.panel.lovelace.editor.card.statistics-graph.periods.day"]),
            ("period_month", ["ui.panel.lovelace.editor.card.statistics-graph.periods.month"]),
            ("period_week", ["ui.panel.lovelace.editor.card.statistics-graph.periods.week"]),
            ("period_5minute", ["ui.panel.lovelace.editor.card.statistics-graph.periods.5minute"]),
            ("week", ["ui.panel.lovelace.editor.card.statistics-graph.periods.week"]),
            ("picture", ["ui.panel.lovelace.editor.card.picture.name"]),
            ("columns", ["ui.panel.lovelace.editor.card.grid.columns"]),
            ("custom", ["ui.panel.lovelace.editor.card.tile.features.types.alarm-modes.modes_list.armed_custom_bypass"]),
            ("welcome_home", ["ui.panel.lovelace.cards.empty_state.title"]),
            ("open_menu", ["ui.panel.lovelace.editor.menu.open"]),
            ("saved", ["ui.panel.lovelace.editor.raw_editor.saved"]),
            ("iframe", ["ui.panel.lovelace.editor.card.iframe.name"]),
            ("horizontal_stack", ["ui.panel.lovelace.editor.card.horizontal-stack.name"]),
            ("drag_and_drop", ["ui.panel.lovelace.cards.shopping-list.drag_and_drop"]),
            ("alarm_modes_label", ["ui.panel.lovelace.editor.features.types.alarm-modes.label"]),
            ("alarm_modes_armed_away", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.armed_away"]),
            ("alarm_modes_armed_home", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.armed_home"]),
            ("alarm_modes_armed_night", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.armed_night"]),
            ("alarm_modes_armed_vacation", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.armed_vacation"]),
            ("alarm_modes_armed_custom_bypass", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.armed_custom_bypass"]),
            ("alarm_modes_disarmed", ["ui.panel.lovelace.editor.features.types.alarm-modes.modes_list.disarmed"]),
            ("buttons", ["ui.panel.lovelace.editor.card.entities.entity_row.buttons"]),
            ("show_more_info", ["ui.panel.lovelace.cards.show_more_info"]),
        ],
    ),
    (  # DEVELOPER-TOOLS
        f"{TRANSLATIONS}/developer-tools",
        [
            ("entity", ["ui.panel.developer-tools.tabs.states.entity"]),
            ("template_editor", ["ui.panel.developer-tools.tabs.templates.editor"]),
            ("set_state", ["ui.panel.developer-tools.tabs.states.set_state"]),
            ("no_entities", ["ui.panel.developer-tools.tabs.states.no_entities"]),
        ],
    ),
]

for _dir, _keys in dir_keys:
    process_dir(_dir, output, _keys)

print(json.dumps(output, indent=2, sort_keys=True))
