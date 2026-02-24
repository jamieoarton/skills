# Create Key Result

Add a Target to a Goal.

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
    "/v2/goal/{goal_id}/key_result": {
      "post": {
        "summary": "Create Key Result",
        "tags": [
          "Goals"
        ],
        "description": "Add a Target to a Goal.",
        "operationId": "CreateKeyResult",
        "parameters": [
          {
            "name": "goal_id",
            "in": "path",
            "description": "900e-462d-a849-4a216b06d930 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "e53a033c"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateKeyResultrequest",
                "required": [
                  "name",
                  "owners",
                  "type",
                  "steps_start",
                  "steps_end",
                  "unit",
                  "task_ids",
                  "list_ids"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "owners": {
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "description": ""
                  },
                  "type": {
                    "description": "Target (key result) types include: `number`, `currency`, `boolean`, `percentage`, or `automatic`.",
                    "type": "string"
                  },
                  "steps_start": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "steps_end": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "task_ids": {
                    "description": "Enter an array of task IDs to link this target with one or more tasks.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "list_ids": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Enter an array of List IDs to link this target with one or more Lists."
                  }
                },
                "examples": [
                  {
                    "name": "New Target Name",
                    "owners": [
                      183
                    ],
                    "type": "number",
                    "steps_start": 0,
                    "steps_end": 10,
                    "unit": "km",
                    "task_ids": [],
                    "list_ids": []
                  }
                ]
              },
              "example": {
                "name": "New Key Result Name",
                "owners": [
                  183
                ],
                "type": "number",
                "steps_start": 0,
                "steps_end": 10,
                "unit": "km",
                "task_ids": [],
                "list_ids": []
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
                  "title": "CreateKeyResultresponse",
                  "required": [
                    "key_result"
                  ],
                  "type": "object",
                  "properties": {
                    "key_result": {
                      "title": "KeyResult",
                      "required": [
                        "id",
                        "goal_id",
                        "name",
                        "type",
                        "unit",
                        "creator",
                        "date_created",
                        "goal_pretty_id",
                        "percent_completed",
                        "completed",
                        "task_ids",
                        "subcategory_ids",
                        "owners",
                        "last_action"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "goal_id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "unit": {
                          "type": "string"
                        },
                        "creator": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "date_created": {
                          "type": "string"
                        },
                        "goal_pretty_id": {
                          "type": "string"
                        },
                        "percent_completed": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "completed": {
                          "type": "boolean"
                        },
                        "task_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "subcategory_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "owners": {
                          "type": "array",
                          "items": {
                            "$ref": "#/paths/~1v2~1goal~1%7Bgoal_id%7D/get/responses/200/content/application~1json/schema/properties/goal/properties/owners/items"
                          },
                          "description": ""
                        },
                        "last_action": {
                          "title": "LastAction",
                          "required": [
                            "id",
                            "key_result_id",
                            "userid",
                            "date_modified",
                            "steps_taken",
                            "note",
                            "steps_before",
                            "steps_current"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "key_result_id": {
                              "type": "string"
                            },
                            "userid": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "date_modified": {
                              "type": "string"
                            },
                            "steps_taken": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "note": {
                              "type": "string"
                            },
                            "steps_before": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "steps_current": {
                              "type": [
                                "string",
                                "null"
                              ]
                            }
                          },
                          "examples": [
                            {
                              "id": "d3183d0f-5cbd-4158-b015-71465f1df269",
                              "key_result_id": "947d46ed-8480-49bc-8c57-e569747efe93",
                              "userid": 183,
                              "date_modified": "1568062902048",
                              "steps_taken": null,
                              "note": "Created Key Result",
                              "steps_before": null,
                              "steps_current": null
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                          "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                          "name": "New Key Result Name",
                          "type": "number",
                          "unit": "km",
                          "creator": 183,
                          "date_created": "1568062902048",
                          "goal_pretty_id": "6",
                          "percent_completed": null,
                          "completed": false,
                          "task_ids": [],
                          "subcategory_ids": [],
                          "owners": [
                            {
                              "id": 183,
                              "username": "John Doe",
                              "email": "example@email.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                              "initials": "JK"
                            }
                          ],
                          "last_action": {
                            "id": "d3183d0f-5cbd-4158-b015-71465f1df269",
                            "key_result_id": "947d46ed-8480-49bc-8c57-e569747efe93",
                            "userid": 183,
                            "date_modified": "1568062902048",
                            "steps_taken": null,
                            "note": "Created Key Result",
                            "steps_before": null,
                            "steps_current": null
                          }
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "key_result": {
                        "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                        "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                        "name": "New Key Result Name",
                        "type": "number",
                        "unit": "km",
                        "creator": 183,
                        "date_created": "1568062902048",
                        "goal_pretty_id": "6",
                        "percent_completed": null,
                        "completed": false,
                        "task_ids": [],
                        "subcategory_ids": [],
                        "owners": [
                          {
                            "id": 183,
                            "username": "John Doe",
                            "email": "example@email.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                            "initials": "JK"
                          }
                        ],
                        "last_action": {
                          "id": "d3183d0f-5cbd-4158-b015-71465f1df269",
                          "key_result_id": "947d46ed-8480-49bc-8c57-e569747efe93",
                          "userid": 183,
                          "date_modified": "1568062902048",
                          "steps_taken": null,
                          "note": "Created Key Result",
                          "steps_before": null,
                          "steps_current": null
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "key_result": {
                    "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                    "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                    "name": "New Key Result Name",
                    "type": "number",
                    "unit": "km",
                    "creator": 183,
                    "date_created": "1568062902048",
                    "goal_pretty_id": "6",
                    "percent_completed": null,
                    "completed": false,
                    "task_ids": [],
                    "subcategory_ids": [],
                    "owners": [
                      {
                        "id": 183,
                        "username": "John Doe",
                        "email": "example@email.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                        "initials": "JK"
                      }
                    ],
                    "last_action": {
                      "id": "d3183d0f-5cbd-4158-b015-71465f1df269",
                      "key_result_id": "947d46ed-8480-49bc-8c57-e569747efe93",
                      "userid": 183,
                      "date_modified": "1568062902048",
                      "steps_taken": null,
                      "note": "Created Key Result",
                      "steps_before": null,
                      "steps_current": null
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
      "name": "Goals"
    }
  ]
}
```