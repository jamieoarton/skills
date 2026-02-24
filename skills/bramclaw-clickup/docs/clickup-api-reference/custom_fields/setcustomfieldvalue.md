# Set Custom Field Value

Add data to a Custom field on a task. \
 \
You'll need to know the `task_id` of the task you want to update, and the universal unique identifier (UUID) `field_id` of the Custom Field you want to set. \
 \
You can use [Get Accessible Custom Fields](ref:getaccessiblecustomfields) or the [Get Task](ref:gettask) endpoint to find the `field_id`.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/task/{task_id}/field/{field_id}": {
      "post": {
        "summary": "Set Custom Field Value",
        "description": "Add data to a Custom field on a task. \\\n \\\nYou'll need to know the `task_id` of the task you want to update, and the universal unique identifier (UUID) `field_id` of the Custom Field you want to set. \\\n \\\nYou can use [Get Accessible Custom Fields](https://developer.clickup.com/reference/getaccessiblecustomfields) or the [Get Task](https://developer.clickup.com/reference/gettask) endpoint to find the `field_id`.",
        "tags": [
          "Custom Fields"
        ],
        "operationId": "SetCustomFieldValue",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "Enter the task ID of the task you want to update.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hv"
              ]
            }
          },
          {
            "name": "field_id",
            "in": "path",
            "description": "Enter the universal unique identifier (UUID) of the Custom Field you want to set.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "b955c4dc"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by its Custom Task ID, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "SetCustomFieldValuerequest",
                "anyOf": [
                  {
                    "type": "object",
                    "title": "URL Custom Field",
                    "description": "The `value` must be a string with a valid URL.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "string",
                        "example": "https://clickup.com/api"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Dropdown Custom Field",
                    "description": "Enter the universal unique identifier (UUID) of the dropdown menu option you want to set. You can find the UUIDs available for each Dropdown Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields) New Dropdown Custom Field options cannot be created from this request.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "string",
                        "example": "uuid1234"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Email Custom Field",
                    "description": "The `value` must be a string with a valid email address.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "string",
                        "example": "user@company.com"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Phone Custom Field",
                    "description": "The `value` must be a string with a valid country code.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "string",
                        "example": "+1 123 456 7890"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Date Custom Field",
                    "description": "The `value` must be Unix time in milliseconds. To display the time in a Date Custom Field in ClickUp, you must include `time: true` in the `value_options` property.",
                    "properties": {
                      "value": {
                        "type": "integer",
                        "format": "int64",
                        "example": 1667367645000
                      },
                      "value_options": {
                        "type": "object",
                        "required": [
                          "time"
                        ],
                        "properties": {
                          "time": {
                            "type": "boolean",
                            "example": true
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Short or Long Text Custom Field",
                    "description": "Enter a string of text.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "string",
                        "example": "This is short or long text in a Custom Field."
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Number Custom Field",
                    "description": "Enter a number.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "number",
                        "example": -28
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Money Custom Field",
                    "description": "You can set an amount, but not the currency of a Money Custom Field via the API. You can check the currency of a Money Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "number",
                        "example": 8000
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Task Relationship Custom Field",
                    "description": "Enter an array of task ids in the `add` property to add them to a Task Relationship Custom Field. Enter them into the `rem` property to remove tasks from the Relationship.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "object",
                        "properties": {
                          "add": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "rem": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "People Custom Field",
                    "description": "Enter an array of user ids or a Team id in the `add` property to add them to a People Custom Field. Enter them into the `rem` property to remove users from a People Custom Field. You can get a list of people in the Workspace using [Get Authorized Teams (Workspaces).](https://developer.clickup.com/reference/getauthorizedteams)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "object",
                        "properties": {
                          "add": {
                            "type": "array",
                            "items": {
                              "type": "number"
                            }
                          },
                          "rem": {
                            "type": "array",
                            "items": {
                              "type": "number"
                            }
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Emoji (Rating) Custom Field",
                    "description": "Enter an integer that is greater than or equal to zero and where the `count` property is greater than or equal to the `value`. You can find the `count` property for each Emoji (Rating) Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "integer",
                        "format": "int32",
                        "example": 4
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Manual Progress Custom Field",
                    "description": "Enter a number between the `start` and `end` values of each Manual Progress Custom Field. For example, for a field with `start: 10` and `end: 30`, sending `current: 20` will be displayed as 50% complete in ClickUp. You can find the `start` and `end` values for each Manual Progress Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "object",
                        "required": [
                          "current"
                        ],
                        "properties": {
                          "current": {
                            "type": "number",
                            "example": 20
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Label Custom Field",
                    "description": "Enter an array of the universal unique identifiers (UUIDs) of the labels you want to apply. You can find the UUIDs available for each Label Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "example": [
                            "uuid1234",
                            "uuid9876"
                          ]
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Location Custom Field",
                    "description": "Include the latitude, longitude, and formatted address as defined in the [Google Maps Geocoding API.](https://developers.google.com/maps/documentation/geocoding/overview)",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "object",
                        "properties": {
                          "location": {
                            "type": "object",
                            "properties": {
                              "lat": {
                                "type": "number"
                              },
                              "lng": {
                                "type": "number"
                              }
                            }
                          },
                          "formatted_address": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "title": "Button Custom Field",
                    "description": "Set a button Custom Field to `true` to \"click\" it. This will trigger the button's action as if it was clicked in the UI.",
                    "required": [
                      "value"
                    ],
                    "properties": {
                      "value": {
                        "type": "boolean",
                        "example": true
                      }
                    }
                  }
                ]
              },
              "examples": {
                "URL Custom Field": {
                  "value": {
                    "value": "https://clickup.com/api"
                  }
                },
                "Dropdown Custom Field": {
                  "value": {
                    "value": "uuid1234"
                  }
                },
                "Email Custom Field": {
                  "value": {
                    "value": "user@company.com"
                  }
                },
                "Phone Custom Field": {
                  "value": {
                    "value": "+1 201 555 0123"
                  }
                },
                "Date Custom Field": {
                  "value": {
                    "value": 1667367645000,
                    "value_options": {
                      "time": true
                    }
                  }
                },
                "Short or Long Text Custom Field": {
                  "value": {
                    "value": "This is short or long text in a Custom Field."
                  }
                },
                "Number Custom Field": {
                  "value": {
                    "value": -28
                  }
                },
                "Money Custom Field": {
                  "value": {
                    "value": 8000
                  }
                },
                "Task Relationship Custom Field": {
                  "value": {
                    "value": {
                      "add": [
                        "abcd1234",
                        "efghi5678"
                      ],
                      "rem": [
                        "jklm9876",
                        "yuiop5678"
                      ]
                    }
                  }
                },
                "People Custom Field": {
                  "value": {
                    "value": {
                      "add": [
                        123,
                        456
                      ],
                      "rem": [
                        987,
                        765
                      ]
                    }
                  }
                },
                "Emoji (Rating) Custom Field": {
                  "value": {
                    "value": 4
                  }
                },
                "Manual Progress Custom Field": {
                  "value": {
                    "value": {
                      "current": 20
                    }
                  }
                },
                "Label Custom Field": {
                  "value": {
                    "value": [
                      "uuid1234",
                      "uuid9876"
                    ]
                  }
                },
                "Location Custom Field": {
                  "value": {
                    "value": {
                      "location": {
                        "lat": -28.016667,
                        "lng": 153.4
                      },
                      "formatted_address": "Gold Coast QLD, Australia"
                    }
                  }
                },
                "Button Custom Field": {
                  "value": {
                    "value": true
                  }
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "examples": [
                    {}
                  ],
                  "contentMediaType": "application/json"
                },
                "example": {}
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Custom Fields"
    }
  ]
}
```