from math import pi

DEFAULT_CAPTURE_ANGLE = pi / 6.0
DEFAULT_PUFF_POWER = (0.7, 2.0)
DEFAULT_JUMP_POWER = (1.2, 2.5)
DEFAULT_RUN_RIGHT_POWER = (1.3, 0.0)
DEFAULT_RUN_LEFT_POWER = (-1.3, 0.0)
DEFAULT_DEPLETE_CONSTANT = 0.1
DEFAULT_DEPLETE_MULTIPLIER = 0.85
DEFAULT_REPEAT_INTERVAL = 0.25

br = lambda s: "{"+s+"}"
qu = lambda s: '"'+s+'"'

    # ActionDef puffDef;
    # ActionDef jumpDef;
    # ActionDef runLeftDef;
    # ActionDef runRightDef;

    # Array<ActionDef> nullList;
    # Array<ActionDef> airList;
    # Array<ActionDef> footList;

    # public void load() {
    #     puffDef = new ActionDef(
    #             -np.pi,
    #             np.pi2,
    #             DEFAULT_PUFF_POWER,
    #             Vector2.Zero,
    #             DEFAULT_DEPLETE_CONSTANT,
    #             DEFAULT_DEPLETE_MULTIPLIER,
    #             DEFAULT_REPEAT_INTERVAL
    #     );

    #     jumpDef = new ActionDef(
    #             DEFAULT_CAPTURE_ANGLE / 2.0f,
    #             np.pi - DEFAULT_CAPTURE_ANGLE,
    #             DEFAULT_JUMP_POWER,
    #             Vector2.Zero,
    #             DEFAULT_DEPLETE_CONSTANT,
    #             DEFAULT_DEPLETE_MULTIPLIER,
    #             DEFAULT_REPEAT_INTERVAL
    #     );

    #     runRightDef = new ActionDef(
    #             -DEFAULT_CAPTURE_ANGLE / 2.0f,
    #             DEFAULT_CAPTURE_ANGLE,
    #             Vector2.Zero,
    #             DEFAULT_RUN_RIGHT_POWER,
    #             DEFAULT_DEPLETE_CONSTANT,
    #             DEFAULT_DEPLETE_MULTIPLIER,
    #             DEFAULT_REPEAT_INTERVAL
    #     );

    #     runLeftDef = new ActionDef(
    #             (np.pi2 - DEFAULT_CAPTURE_ANGLE) / 2.0f,
    #             DEFAULT_CAPTURE_ANGLE,
    #             Vector2.Zero,
    #             DEFAULT_RUN_LEFT_POWER,
    #             DEFAULT_DEPLETE_CONSTANT,
    #             DEFAULT_DEPLETE_MULTIPLIER,
    #             DEFAULT_REPEAT_INTERVAL
    #     );