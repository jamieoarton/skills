# Get Task

View information about a task. You can only view task information of tasks you can access. \
 \
Tasks with attachments will return an "attachments" response. \
 \
Docs attached to a task are not returned.

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
    "/v2/task/{task_id}": {
      "get": {
        "summary": "Get Task",
        "tags": [
          "Tasks"
        ],
        "description": "View information about a task. You can only view task information of tasks you can access. \\\n \\\nTasks with attachments will return an \"attachments\" response. \\\n \\\nDocs attached to a task are not returned.",
        "operationId": "GetTask",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hz"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by its custom task id, this value must be `true`.",
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
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "include_subtasks",
            "in": "query",
            "description": "Include subtasks, default false",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_markdown_description",
            "in": "query",
            "description": "To return task descriptions in Markdown format, use `?include_markdown_description=true`.",
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
            "name": "custom_fields",
            "in": "query",
            "description": "Include tasks with specific values in one or more Custom Fields. Custom Relationships are included.\\\n \\\nFor example: `?custom_fields=[{\"field_id\":\"abcdefghi12345678\",\"operator\":\"=\",\"value\":\"1234\"},{\"field_id\":\"jklmnop123456\",\"operator\":\"<\",\"value\":\"5\"}]`\\\n \\\nOnly set Custom Field values display in the `value` property of the `custom_fields` parameter. If you want to include tasks with specific values in only one Custom Field, use `custom_field` instead.\\\n \\\nLearn more about [filtering using Custom Fields.](https://developer.clickup.com/docs/filtertasks)",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetTaskresponse",
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "custom_id": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "custom_item_id": {
                      "type": [
                        "number",
                        "null"
                      ],
                      "description": "The custom task type ID for this task. A value of `null` represents task type \"Task\".\\\n \\\nTo get a list of available custom task type IDs for your Workspace, use the [Get Custom Task Types endpoint](https://developer.clickup.com/reference/getcustomitems)."
                    },
                    "name": {
                      "type": "string"
                    },
                    "text_content": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    },
                    "status": {
                      "title": "Status",
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "status": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "orderindex": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "p7001234_FxGmgrnk",
                          "status": "in progress",
                          "color": "#d3d3d3",
                          "orderindex": 1,
                          "type": "custom"
                        }
                      ]
                    },
                    "orderindex": {
                      "type": "string"
                    },
                    "date_created": {
                      "type": "string"
                    },
                    "date_updated": {
                      "type": "string"
                    },
                    "date_closed": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "creator": {
                      "title": "Creator",
                      "required": [
                        "id",
                        "username",
                        "color",
                        "profilePicture"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "username": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "profilePicture": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": 183,
                          "username": "John Doe",
                          "color": "#827718",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                        }
                      ]
                    },
                    "assignees": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": ""
                    },
                    "watchers": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": ""
                    },
                    "checklists": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": ""
                    },
                    "tags": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": ""
                    },
                    "parent": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "priority": {
                      "title": "Priority",
                      "type": "object",
                      "nullable": true,
                      "properties": {
                        "color": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "orderindex": {
                          "type": "string"
                        },
                        "priority": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "color": "#f8ae00",
                          "id": "3",
                          "orderindex": "3",
                          "priority": "normal"
                        }
                      ]
                    },
                    "due_date": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "start_date": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "points": {
                      "type": [
                        "number"
                      ]
                    },
                    "time_estimate": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "time_spent": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "custom_fields": {
                      "type": "array",
                      "items": {
                        "title": "CustomFields8",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "type": {
                            "type": "string"
                          },
                          "type_config": {
                            "title": "TypeConfig1",
                            "type": "object",
                            "properties": {
                              "single_user": {
                                "type": "boolean"
                              },
                              "include_groups": {
                                "type": "boolean"
                              },
                              "include_guests": {
                                "type": "boolean"
                              },
                              "include_team_members": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {}
                            ]
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "hide_from_guests": {
                            "type": "boolean"
                          },
                          "value": {
                            "oneOf": [
                              {
                                "title": "Value",
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "integer",
                                    "contentEncoding": "int32"
                                  },
                                  "username": {
                                    "type": "string"
                                  },
                                  "email": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  },
                                  "initials": {
                                    "type": "string"
                                  },
                                  "profilePicture": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  }
                                }
                              },
                              {
                                "title": "Value1",
                                "required": [
                                  "id",
                                  "username",
                                  "email",
                                  "color",
                                  "initials",
                                  "profilePicture"
                                ],
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "type": "integer",
                                    "contentEncoding": "int32"
                                  },
                                  "username": {
                                    "type": "string"
                                  },
                                  "email": {
                                    "type": "string"
                                  },
                                  "color": {
                                    "type": "string"
                                  },
                                  "initials": {
                                    "type": "string"
                                  },
                                  "profilePicture": {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  }
                                },
                                "examples": [
                                  {
                                    "id": 183,
                                    "username": "John Doe",
                                    "email": "john@example.com",
                                    "color": "#7b68ee",
                                    "initials": "JD",
                                    "profilePicture": null
                                  }
                                ]
                              },
                              {
                                "title": "Value2",
                                "required": [
                                  "value"
                                ],
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "type": "string"
                                  }
                                },
                                "example": [
                                  "This is a text CF"
                                ]
                              }
                            ],
                            "examples": [
                              {
                                "id": 183,
                                "username": "John Doe",
                                "email": "john@example.com",
                                "color": "#7b68ee",
                                "initials": "JD",
                                "profilePicture": null
                              },
                              {
                                "value": null
                              }
                            ]
                          },
                          "value_richtext": {
                            "type": "string"
                          },
                          "value_markdown": {
                            "type": "string"
                          },
                          "required": {
                            "type": "boolean"
                          }
                        }
                      },
                      "description": ""
                    },
                    "locations": {
                      "type": "array",
                      "items": {
                        "title": "ListLocation",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "The ID of the List where the task has been added."
                          },
                          "name": {
                            "type": "string",
                            "description": "The name of the List where the task has been added."
                          }
                        },
                        "examples": [
                          {
                            "id": "123456789",
                            "name": "Secondary List"
                          }
                        ]
                      },
                      "description": "Array of Lists where the task has been added."
                    },
                    "list": {
                      "title": "List",
                      "required": [
                        "id"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "123"
                        }
                      ]
                    },
                    "folder": {
                      "title": "Folder",
                      "required": [
                        "id"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "456"
                        }
                      ]
                    },
                    "space": {
                      "title": "Space",
                      "required": [
                        "id"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "789"
                        }
                      ]
                    },
                    "url": {
                      "type": "string"
                    },
                    "markdown_description": {
                      "type": "string"
                    },
                    "attachments": {
                      "type": "array",
                      "items": {
                        "title": "Attachment",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "date": {
                            "type": "integer",
                            "format": "int64"
                          },
                          "title": {
                            "type": "string"
                          },
                          "type": {
                            "type": "integer"
                          },
                          "source": {
                            "type": "integer"
                          },
                          "version": {
                            "type": "integer"
                          },
                          "extension": {
                            "type": "string"
                          },
                          "thumbnail_small": {
                            "type": "string"
                          },
                          "thumbnail_medium": {
                            "type": "string"
                          },
                          "thumbnail_large": {
                            "type": "string"
                          },
                          "is_folder": {
                            "type": "boolean"
                          },
                          "mimetype": {
                            "type": "string"
                          },
                          "hidden": {
                            "type": "boolean"
                          },
                          "parent_id": {
                            "type": "string"
                          },
                          "size": {
                            "type": "integer",
                            "format": "int64"
                          },
                          "total_comments": {
                            "type": "integer"
                          },
                          "resolved_comments": {
                            "type": "integer"
                          },
                          "user": {
                            "type": "string",
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1stop/post/responses/200/content/application~1json/schema/properties/data/properties/user"
                          },
                          "deleted": {
                            "type": "boolean"
                          },
                          "orientation": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          },
                          "email_data": {
                            "type": "object"
                          },
                          "url_w_query": {
                            "type": "string"
                          },
                          "url_w_host": {
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": "62447c77-2086-4cda-b274-f53eccf0547b.csv",
                            "date": 1711570108374,
                            "title": "Canny - Exported posts - 2024-03-09.csv",
                            "type": 1,
                            "source": 1,
                            "version": 0,
                            "extension": "csv",
                            "thumbnail_small": null,
                            "thumbnail_medium": null,
                            "thumbnail_large": null,
                            "is_folder": null,
                            "mimetype": "text/csv",
                            "hidden": false,
                            "parent_id": "36fjfqy",
                            "size": 140970,
                            "total_comments": 0,
                            "resolved_comments": 0,
                            "user": [
                              {
                                "id": 123,
                                "username": "John Doe",
                                "initials": "JD",
                                "email": "user@company.com",
                                "color": "#000000",
                                "profilePicture": "https://clickup.com/avatar.jpg"
                              }
                            ],
                            "deleted": false,
                            "orientation": null,
                            "url": "https://t6931406.p.clickup-attachments.com/t6931406/62447c77-2086-4cda-b274-f53eccf0547b/Canny%20-%20Exported%20posts%20-%202024-03-09.csv",
                            "email_data": null,
                            "url_w_query": "https://t6931406.p.clickup-attachments.com/t6931406/62447c77-2086-4cda-b274-f53eccf0547b/Canny%20-%20Exported%20posts%20-%202024-03-09.csv?view=open",
                            "url_w_host": "https://t6931406.p.clickup-attachments.com/t6931406/62447c77-2086-4cda-b274-f53eccf0547b/Canny%20-%20Exported%20posts%20-%202024-03-09.csv"
                          }
                        ]
                      }
                    }
                  }
                }
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
      "name": "Tasks"
    }
  ]
}
```